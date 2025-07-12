import random
import numpy as np
import matplotlib.pyplot as plt
from deap import base, creator, tools, algorithms

# Number of cities
NUM_CITIES = 10

# Generate random city coordinates
cities = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(NUM_CITIES)]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Function to calculate total distance of a given route
def route_distance(route):
    dist = 0
    for i in range(len(route) - 1):
        dist += distance(cities[route[i]], cities[route[i+1]])
    dist += distance(cities[route[-1]], cities[route[0]])  # Return to start city
    return dist

# Evaluation function for DEAP
def eval_tsp(individual):
    return (route_distance(individual),)  # Needs to return a tuple

# Setting up DEAP's creator and toolbox
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# Register functions for Genetic Algorithm
toolbox.register("indices", random.sample, range(NUM_CITIES), NUM_CITIES)  # Random permutation of cities
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("mate", tools.cxOrdered)  # Ordered crossover
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.1)  # Swap mutation
toolbox.register("select", tools.selTournament, tournsize=3)  # Tournament selection
toolbox.register("evaluate", eval_tsp)

# Genetic Algorithm Parameters
POP_SIZE = 100
GENS = 500
MUTPB = 0.2
CXPB = 0.7

# Main function to run the genetic algorithm
def run_ga():
    # Create initial population
    population = toolbox.population(n=POP_SIZE)

    # Run the genetic algorithm
    algorithms.eaSimple(population, toolbox, cxpb=CXPB, mutpb=MUTPB, ngen=GENS, stats=None, halloffame=None, verbose=True)

    # Find the best route
    best_individual = tools.selBest(population, k=1)[0]
    print(f"Best Route: {best_individual}, Distance: {route_distance(best_individual)}")
    
    # Plot the best route
    plot_route(best_individual)

def plot_route(route):
    route_cities = [cities[i] for i in route] + [cities[route[0]]]
    x_vals, y_vals = zip(*route_cities)
    plt.figure(figsize=(10, 8))
    plt.plot(x_vals, y_vals, 'bo-', label='Route')
    plt.scatter(*zip(*cities), c='r', label='Cities', s=50)
    for i, city in enumerate(cities):
        plt.text(city[0] + 2, city[1] + 2, f'{i}', fontsize=12)
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.title("Best Route for TSP")
    plt.legend()
    plt.show()

# Run the Genetic Algorithm
run_ga()