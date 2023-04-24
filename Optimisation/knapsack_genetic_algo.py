import plotly.express as px
import numpy as np
import random
from typing import Tuple, List
from dataclasses import dataclass


@dataclass
class ItemsInfo:
    values: List[int]
    weights: List[int]
    threshold: int


@dataclass
class HyperParameters:
    generations: int
    mutation_rate: float
    population_size: int


class GeneticAlgorithm:

    def __init__(self, items_info: ItemsInfo, hyper_parameters: HyperParameters):
        self.values = items_info.values
        self.weights = items_info.weights
        self.threshold = items_info.threshold
        self.generations = hyper_parameters.generations
        self.mutation_rate = hyper_parameters.mutation_rate
        self.population_size = hyper_parameters.population_size

    def is_valid(self, chromosome: List[int]) -> bool:
        total_weight = sum(self.weights[item] * chromosome[item] for item in range(len(chromosome)))
        return total_weight <= self.threshold

    def fitness(self, chromosome: List[int]) -> int:
        if not self.is_valid(chromosome):
            return 0
        return sum(self.values[item] * chromosome[item] for item in range(len(chromosome)))

    def generate_initial_population(self) -> List[List[int]]:
        population = [[random.randint(0, 1) for _ in range(len(self.weights))] for _ in range(self.population_size)]
        return population

    def selection(self, population: List[List[int]]):
        fitness_list = [self.fitness(chromosome) for chromosome in population]
        total_fitness = sum(fitness_list)
        probabilities = [fitness / total_fitness if total_fitness != 0 else 0 for fitness in fitness_list]
        return random.choices(population, weights=probabilities, k=2)

    def crossover(self, parents: List[List[int]]) -> Tuple[List[int], List[int]]:
        point = random.randint(1, len(parents[0]) - 1)
        child1 = parents[0][:point] + parents[1][point:]
        child2 = parents[1][:point] + parents[0][point:]
        return child1, child2

    def mutation(self, chromosome: List[int]) -> List[int]:
        for i in range(len(chromosome)):
            if random.random() < self.mutation_rate:
                chromosome[i] = 1 - chromosome[i]
        return chromosome

    def run(self) -> Tuple[List[int], int, List[int], int]:

        initial_population = self.generate_initial_population()
        population = initial_population

        score_list = []

        for generation in range(self.generations):
            parents = self.selection(population)
            children = self.crossover(parents)
            children = [self.mutation(child) for child in children]
            population = sorted(population + children, key=lambda chromosome: -self.fitness(chromosome))[:self.population_size]

            best_solution = max(population, key=self.fitness)
            best_fitness = self.fitness(best_solution)
            score_list.append(best_fitness)

        final_solution = max(population, key=self.fitness)
        final_fitness = self.fitness(final_solution)
        total_weight_final = sum(self.weights[item] * final_solution[item] for item in range(len(final_solution)))

        return final_solution, final_fitness, score_list, total_weight_final


# Initialise our knapsack and hyperparameters
num_items = 100
weights = np.random.randint(1, 15, size=num_items)
values = np.random.randint(10, 50, size=num_items)
items_info = ItemsInfo(values=list(values), weights=list(weights), threshold=300)
hyper_parameters = HyperParameters(generations=2500, mutation_rate=0.1, population_size=500)

# Run the genetic algorithm
ga_algo = GeneticAlgorithm(items_info=items_info, hyper_parameters=hyper_parameters)
best_solution, best_score, scores, total_weight = ga_algo.run()

# Plot the algorithm
fig = px.line(x=range(len(scores)), y=scores, labels={'y': 'Score', 'x': 'Generations'})
fig.update_layout(template="simple_white", font=dict(size=18),
                  title_text='Score Progression', width=650,
                  title_x=0.5, height=400)
fig.show()
