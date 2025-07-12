import random

def fitness(x):
    return x**2 

# create the initial population(random value between -10 and 10)
def create_population(pop_size):
    return [random.uniform(-10, 10) for _ in range(pop_size)]

# selection function- tournament selection
def select(population):
    tournament_size = 3
    tournament = random.sample(population, tournament_size)
    return max(tournament, key=fitness)

def crossover(parent1, parent2):
    crossover_point = random.random()
    child1 = crossover_point*parent1+(1 - crossover_point)*parent2
    child2 = (1 - crossover_point) * parent1 + crossover_point * parent2
    return child1,child2 

# mutation function - small random change
def mutate(child):
    mutation_rate = 0.1
    if random.random() < mutation_rate:
        return child + random.uniform(-1, 1)
    return child

# main genetic algorithm
def gentic_algorithm(pop_size = 20, generations = 100):
    population = create_population(pop_size)
    for generation in range(generations):
        #Select the best parents
        parents =[select(population)for _ in range(pop_size//2)]
#creossover and create offspring 
    offspring = []
    for i in range(0,len(parents),2):
        child1,child2=crossover(parents[i],parents[i+1])
        offspring.append(mutate(child1))
        offspring.append(mutate(child2))
        #evaluate the fitness of the offspring
        population = sorted(population + offspring, key=fitness,reverse=True)[:pop_size]
        #print the best individual in each generation
        best_individual = max(population,key=fitness)
        print(f"Generation{generation}:Best solution = {best_individual},Fitness = {fitness(best_individual)}")
    return max(population,key=fitness)
#Run the genetic algorithm 
best_solution = gentic_algorithm()
print(f"Best solution found :{best_solution},Fitness:{fitness(best_solution)}")
