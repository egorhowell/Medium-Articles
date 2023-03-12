import numpy as np


class HillClimb:

    def __init__(self,
                 initial_solution: list,
                 cities: dict):
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

            distance += self.euclidean_distance(self.cities[city1][0], self.cities[city2][0],
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
    def get_neighbourhood_solutions(tour: list,
                                    ) -> list:
        """Lists all neighbouring tours."""

        neighbourhood_solutions = []

        for i in range(1, len(tour) - 1):
            for j in range(1, len(tour) - 1):
                if i == j:
                    continue

                neighbourhood_solutions.append(HillClimb.swap_positions(tour, i, j))

        return neighbourhood_solutions

    def get_best_solution(self,
                          neighbourhood_solutions,
                          ) -> list:
        """Get the best tour from a list of routes."""

        best_solution = neighbourhood_solutions[0]
        for solution in neighbourhood_solutions:
            if self.tour_distance(solution) < self.tour_distance(best_solution):
                best_solution = solution.copy()
        return best_solution

    def run_hill_climb(self,
                       iterations: int,
                       ) -> list:
        """Running the tabu search."""

        best_solution = self.initial_solution.copy()

        for _ in range(iterations):

            current_solution = self.get_best_solution(self.get_neighbourhood_solutions(best_solution))
            if self.tour_distance(current_solution) < self.tour_distance(best_solution):
                best_solution = current_solution.copy()
            else:
                break

        return best_solution
