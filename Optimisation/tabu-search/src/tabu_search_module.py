import numpy as np


class TabuSearch:

    def __init__(self, initial_solution: list, cities: dict):
        self.initial_solution = initial_solution
        self.cities = cities

    @staticmethod
    def euclidean_distance(cord_x1: float,
                           cord_x2: float,
                           cord_y1: float,
                           cord_y2: float) -> float:
        """Returns the distance between two cities."""
        return np.sqrt((cord_x1 - cord_x2) ** 2 + (cord_y1 - cord_y2) ** 2)

    def tour_distance(self,
                      tour: list,
                      ) -> float:
        """Computes the distance of a tour."""
        distance = 0.0

        for index, _ in enumerate(tour):
            if index + 1 >= len(tour):
                break

            city1 = tour[index]
            city2 = tour[index + 1]

            distance += TabuSearch.euclidean_distance(self.cities[city1][0], self.cities[city2][0],
                                                      self.cities[city1][1], self.cities[city2][1])

        return distance

    @staticmethod
    def swap_positions(tour: list,
                       city1_idx: int,
                       city2_idx: int,
                       ) -> list:
        """Swaps two cities in a given tour."""

        tour_copy = tour.copy()
        tour_copy[city1_idx], tour_copy[city2_idx] = tour_copy[city2_idx], tour_copy[city1_idx]
        return tour_copy

    @staticmethod
    def get_neighboorhood_solutions(tour: list,
                                    ) -> list:
        """Lists all neighbouring tours."""

        neighboorhood_solutions = []

        for i in range(1, len(tour) - 1):
            for j in range(1, len(tour) - 1):
                if i == j:
                    continue

                neighboorhood_solutions.append(TabuSearch.swap_positions(tour, i, j))

        return neighboorhood_solutions

    def run_tabu_search(self,
                        iterations: int,
                        tabu_size: int,
                        ) -> list:
        """Running the tabu search."""

        best_solution = self.initial_solution
        best_candidate = self.initial_solution
        tabu_list = [self.initial_solution]

        for _ in range(iterations):

            solution_neighboorhood = self.get_neighboorhood_solutions(best_candidate)
            best_candidate = solution_neighboorhood[0]

            for candidate in solution_neighboorhood:
                if (self.tour_distance(candidate) < self.tour_distance(best_candidate)) and (
                        candidate not in tabu_list):
                    best_candidate = candidate

            if self.tour_distance(best_candidate) < self.tour_distance(best_solution):
                best_solution = best_candidate

            tabu_list.append(best_candidate)
            if len(tabu_list) > tabu_size:
                tabu_list.pop(0)

        return best_solution
