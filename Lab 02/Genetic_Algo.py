import random
import numpy as np


def fitness_function(populations, query):

    fitness_list = []

    for temporary_state in populations:
        # test 4
        # print("ekhane")
        max_fitness = (query*(query-1))/2
        x_diagonal = []
        y_diagonal = []
        # matrix for finding pairs easier
        matrix = np.zeros(shape=(len(temporary_state), len(temporary_state)))
        for i in range(len(temporary_state)):
            x = temporary_state[i]
            matrix[len(temporary_state) - x - 1][i] = 1
            x_diagonal.append(len(temporary_state) - x)
            y_diagonal.append(i)
        rows_atk_total = 0

        for i in range(len(temporary_state)):
            # test 1
            # print("ami ekhane")
            sumRow = np.sum(matrix[i], dtype=int)
            attPairsInThisRow = (sumRow*(sumRow-1))/2
            rows_atk_total += attPairsInThisRow
        diagonal_atk_total = 0

        for i in range(len(x_diagonal)):
            # test 2
            # print("ami ebar ekhane")
            diagonal_atk = 0 
            sliced_x = x_diagonal[i + 1:]
            sliced_y = y_diagonal[i + 1:]

            for j in range(len(sliced_x)):
                # test 3
                # print("ami ekebare ekkhane")
                if(abs(x_diagonal[i]-sliced_x[j]) == abs(y_diagonal[i]-sliced_y[j])):
                    diagonal_atk = diagonal_atk+1
            diagonal_atk_total = diagonal_atk_total+diagonal_atk

        atk_pairs = diagonal_atk_total + rows_atk_total
        fitness = max_fitness - atk_pairs
        fitness_list.append(fitness)
    return fitness_list


def crossover(x, y):
    # generating single random crossover point
    cross_over_point = np.random.randint(0, queens, dtype=int)
    child_first = x[cross_over_point:]
    child_second = y[:cross_over_point]
    return child_first + child_second


def mutation(channel):
    random_index = np.random.randint(0, queens)
    random_position = np.random.randint(0, queens)
    channel[random_index] = random_position
    return channel


def selection(pop, population_fitness):

    fitness_prob = []

    for i in range(len(population_fitness)):
        fitness_prob.append(
            (population_fitness[i] / sum(population_fitness)))

    a = [0 for i in range(len(population))]
    for i in range(len(population)):
        a[i] = i

    size = 1

    return pop[np.random.choice(a, size, True, fitness_prob)[0]]


def state(query):
    pop = [random.randint(1, query) for i in range(query)]
    return pop


def genetic_algo(pop, q, mut_tr=0.3):
    max_fitness = (q * (q - 1))/2
    generation = 0
    while True:
        generation += 1

        new_pop = []
        allFitness = fitness_function(pop, q)
        if generation % 1000 == 0:
            print("Max fit -{} Generation {} ".format(max(allFitness), generation))

        if max(allFitness) == max_fitness or generation == 200000:
            return (pop, allFitness, generation)
        for _ in range(len(pop)):
            x = selection(pop, allFitness)
            y = selection(pop, allFitness)
            child = crossover(x, y)
            if(np.random.random() < mut_tr):
                child = mutation(child)

            new_pop.append(child)

        pop = new_pop


if __name__ == "__main__":

    queens = int(input())
    starting_population_size = 10
    population = [state(queens) for i in range(starting_population_size)]
    popu, fit, generation = genetic_algo(population, queens)
    print("Child {}, Max Fitness {}, Generation {}".format(
        popu[fit.index(max(fit))], max(fit), generation))
