import random

#task durations in hrs
task_times = [5, 8, 4, 7, 6, 3, 9]

#Facility capacities in hrs/day
capacities = [24, 30, 28]

# Cost matrix [task][facility]
cost_matrix = [
    [10, 12, 9],
    [15, 14, 16],
    [8, 9, 7],
    [12, 10, 13],
    [14, 13, 12],
    [9, 8, 10],
    [11, 12, 13]
]

POP_SIZE = 6 #number of inital chromosomes
CROSSOVER_RATE = 0.8 #rate at which crossover will be applied to parents
MUTATION_RATE = 0.2 #rate at which randomly the children values will be mutated
NUM_GENERATIONS = 20 #times the algorithm would iterate

#Initialize the intial population with random chromosomes or values
def generate_chromosome():
    return [random.randint(0, 2) for _ in range(len(task_times))]

#calculating fitness values of all the chromosomes 
#lower fitness score equals a better solution
def calculate_fitness(chrom):
    total_time = [0, 0, 0] #list to track time allocated to each facility
    total_cost = 0

    for i, facility in enumerate(chrom):
        time = task_times[i]
        total_time[facility] += time
        total_cost += time * cost_matrix[i][facility]

    penalty = 0
    #for exceeding capacity or a constrait a penalty is impose on the fitness score
    for i in range(3):
        if total_time[i] > capacities[i]:
            penalty += (total_time[i] - capacities[i]) * 100  #heavy penalty

    return total_cost + penalty

#selecting the fittest chromosomes from the population randomly
def roulette_wheel_selection(population, fitnesses):
    total_fitness = sum(1/f for f in fitnesses)
    pick = random.uniform(0, total_fitness)
    current = 0
    for i, f in enumerate(fitnesses):
        current += 1/f
        if current > pick:
            return population[i]

#mixing parent values to create offsprings
def one_point_crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 2)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(chrom):
    i, j = random.sample(range(len(chrom)), 2)
    chrom[i], chrom[j] = chrom[j], chrom[i]

#carries out the genetic algorithm 20 times based on the defined contraints
def evolve():
    #generating random populations
    population = [generate_chromosome() for _ in range(POP_SIZE)]

    for gen in range(NUM_GENERATIONS):
        #calculating fitness of each chromosome in the population
        fitnesses = [calculate_fitness(ch) for ch in population]
        print(f"Generation {gen+1} Best fitness: {min(fitnesses)}")

        new_population = []

        # Selection and Crossover
        while len(new_population) < POP_SIZE:
            p1 = roulette_wheel_selection(population, fitnesses)
            p2 = roulette_wheel_selection(population, fitnesses)

            if random.random() < CROSSOVER_RATE:
                c1, c2 = one_point_crossover(p1, p2)
            else:
                c1, c2 = p1[:], p2[:]

            new_population.extend([c1, c2])

        # Mutation
        for i in range(len(new_population)):
            if random.random() < MUTATION_RATE:
                mutate(new_population[i])

        population = new_population[:POP_SIZE]

    # Final result
    fitnesses = [calculate_fitness(ch) for ch in population]
    best_idx = fitnesses.index(min(fitnesses))
    best_solution = population[best_idx]

    print("\nBest Task Assignment (Task i -> Facility j):")
    for i, f in enumerate(best_solution):
        print(f"Task {i+1} -> Facility {f+1}")
    print("Minimum Total Cost:", fitnesses[best_idx])

evolve()
