import itertools
import math
from typing import List, Tuple


class BruteForceSearch:
    """
    A class that performs a brute force search for the optimal route between a list of cities.

    Attributes:
        cities: A list of tuples representing the cities as ((name, x, y) coordinates.
    """

    def __init__(self, cities: List[Tuple[str, float, float]]):
        """
        Initializes a new instance of the BruteForceSearch class.

        Args:
            cities: A list of tuples representing the cities as ((name, x, y) coordinates.
        """

        self.cities = cities

    def _calculate_city_distance(
        self, city1: Tuple[str, float, float], city2: Tuple[str, float, float]
    ) -> float:
        """
        Calculates the Euclidean distance between two cities represented as tuples (name, x, y).

        Args:
            city1: A tuple representing the coordinates of the first city (name, x, y)
            city2: A tuple representing the coordinates of the second city (name, x, y)

        Returns:
            The Euclidean distance between the two cities.
        """
        _, x1, y1 = city1
        _, x2, y2 = city2
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def _calculate_route_distance(self, route: List[Tuple[str, float, float]]) -> float:
        """
        Calculates the total distance of the route between a list of cities.

        Args:
            route: A list of tuples representing the cities as ((name, x, y) coordinates.

        Returns:
            The total distance of the route.
        """

        if not route:
            raise ValueError("Cannot calculate the distance for an empty or none route")

        total_distance = sum(
            self._calculate_city_distance(route[i], route[i + 1])
            for i in range(len(route) - 1)
        )
        return total_distance

    def run(self) -> Tuple[float, List[Tuple[str, float, float]]]:
        """
        Calculates the optimal route using a brute force approach.
        Args:
            None.
        Returns:
            A tuple containing the total distance of the optimal route and the corresponding route.
        """
        if len(self.cities) < 3:
            raise ValueError(
                "There must be at least 3 cities to compute the optimal route"
            )

        # Generate all permutations of the remaining cities
        remaining_cities = self.cities[1:-1]
        perms = itertools.permutations(remaining_cities)

        # Extract the start and end cities
        start = self.cities[0]
        end = self.cities[-1]

        # Concatenate the start and end cities to each permutation
        permutations = [[start] + list(p) + [end] for p in perms]

        # Compute all the possible solutions
        solutions = [
            (self._calculate_route_distance(route), list(route))
            for route in permutations
        ]

        # Get the best solution
        best_solution = min(solutions, key=lambda x: x[0])
        best_distance, best_route = best_solution

        return best_distance, best_route
