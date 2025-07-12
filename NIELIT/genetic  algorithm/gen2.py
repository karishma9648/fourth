import random
import numpy as np 
import matplotlib.pyplot as plt 
from deap import base ,creator,tools,algorithms
#Numbers of cities 
NUM_CITIES=10
#Generati
cities =[{random.randint(0,100),random.randint(0,100)}for _ in range(NUM_CITIES)] 
#Function to calculate Euclidean distance between two cities 
def distance(city1,city2):
    return np.sqrt((city1[0]- city2[0])**2+(city1[1] - city2[1])**)
#Function to calculate the total distance of a route 
def route_distance(route):
    dist = 0
    for i in range (len(route)-1):
        dist += distance(cities[route[i],cities[route[i+1]])
        dist += distance(cities[route[-1],cities[route[0]])
                         return dist
                         def eval_tsp(individual):
                         return(route_distance(individual),)
                         creator.create("FitnessMin", base.Fitness,weights=(-1.0))
                         creator.create("individual",list,fitness= creator.FitnessMin)
                         toolbox = base.Toolbox()   
                         toolbox.register("indices",random.sample,range(NUM_CITIES),NUM_CITIES)
                         toolbox.register("individual", tools.initIterate, creator.individual, toolbox.individual)
                         toolbox.register("population", tools.initRepeat, list, toolbox.individual)
                         toolbox.register("mate", tools.cxOrdered)
                         toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.1)
                         toolbox.register("select", tools.selTournament, tournsize=3)
                         toolbox.register("evaluate", eval_tsp)
                         POP_SIZE =100
                         GENS=500
                         MUTPB=0.2
                         CXPB=0.7
                         def run_ga():
                         population = toolbox.population(n=POP_SIZE)
                         #Run the genetic algorithm
                         algorithms.eaSimple(population,toolbox,cxpb=CXPB,mutpb=MUTPB,ngen=GENS,stats=None,halloffame=None,verbose=True)
def plot_route(route):
route_ciyies
                      
                         


                         
                         