# Import packages
import logging
import os
import time
from typing import List, Tuple

import numpy as np
import plotly.express as px
from brute_force_search import BruteForceSearch
from faker import Faker

logger = logging.getLogger(__name__)


def generate_cities(n_cities: int) -> List[Tuple[str, float, float]]:
    """
    Generates a list of n cities with random coordinates and labels.
    Args:
        n_cities: The number of cities to generate.
    Returns:
        A list of tuples representing the cities as ((name, x, y) coordinates).
    """
    x = np.random.randint(0, 10, n_cities)
    y = np.random.randint(0, 10, n_cities)
    labels = [Faker().city() for _ in range(n_cities)]
    cities = [(labels[i], x[i], y[i]) for i in range(n_cities)]
    cities.append(cities[0])
    return cities


def run_brute_force(n_cities: int) -> float:
    """Runs the brute force search for a certain number of cities.
    Args:
        n_cities: The number of cities to generate and run the search on.
    Returns:
        The elapsed time for the search in seconds.
    """
    cities = generate_cities(n_cities)

    start_time = time.time()

    bfs = BruteForceSearch(cities)
    best_distance, best_route = bfs.run()

    end_time = time.time()
    elapsed_time = end_time - start_time

    logger.info(f"Elapsed time for {n_cities} cities: {elapsed_time:.4f} seconds")

    return elapsed_time


def main():
    logging.basicConfig(level=logging.INFO)

    number_cities = list(range(3, 13))
    times = []

    for num in number_cities:
        elapsed_time = run_brute_force(n_cities=num)
        times.append(elapsed_time)

    fig = px.line(x=number_cities, y=times)
    fig.update_layout(
        title_text="Combinatorial Explosion Example",
        title_x=0.5,
        font=dict(size=18),
        xaxis=dict(title="Number of Cities", titlefont=dict(size=18)),
        yaxis=dict(title="Duration of Brute-Force (Seconds)", titlefont=dict(size=18)),
        width=800,
        height=500,
        template="simple_white",
    )

    if not os.path.exists("../images"):
        os.mkdir("../images")
    fig.write_image("../images/combinatorial_explosion.png")

    fig.show()


if __name__ == "__main__":
    main()
