import random
import numpy as np
import matplotlib.pyplot as plt
from deap import base, creator, tools, algorithms

# Number of cities
NUM_CITIES = 10

# Generate random city coordinates (x, y)
cities = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(NUM_CITIES)]

def distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def route_distance(route):
    """Calculate total distance of a given route."""
    dist = 0
    for i in range(len(route) - 1):
        dist += distance(cities[route[i]], cities[route[i + 1]])
    dist += distance(cities[route[-1]], cities[route[0]])  # Returning to start city
    return dist

def eval_tsp(individual):
    """Evaluation function for TSP (Traveling Salesman Problem)."""
    return (route_distance(individual),)

# Define DEAP framework classes
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(NUM_CITIES), NUM_CITIES)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("evaluate", eval_tsp)

# Genetic Algorithm Parameters
POP_SIZE = 100
GENS = 500
MUTPB = 0.2
CXPB = 0.7

def run_ga():
    """Runs the Genetic Algorithm."""
    population = toolbox.population(n=POP_SIZE)
    
    # Run the genetic algorithm
    algorithms.eaSimple(population, toolbox, cxpb=CXPB, mutpb=MUTPB, ngen=GENS,
                        stats=None, halloffame=None, verbose=True)
    
    return tools.selBest(population, 1)[0]  # Return the best route

def plot_route(route):
    """Plots the best TSP route."""
    route_cities = [cities[i] for i in route] + [cities[route[0]]]  # Complete cycle
    x_vals, y_vals = zip(*route_cities)

    plt.figure(figsize=(10, 8))
    plt.plot(x_vals, y_vals, 'bo-', label='Cities', zorder=5)
    
    for i, city in enumerate(cities):
        plt.text(city[0] + 2, city[1] + 2, f'{i}', fontsize=12)

    plt.xlabel('X Coordinates')
    plt.ylabel('Y Coordinates')
    plt.title("Best Route for TSP")
    plt.legend()
    plt.show()

# Run the Genetic Algorithm and plot the best route
best_route = run_ga()
plot_route(best_route)