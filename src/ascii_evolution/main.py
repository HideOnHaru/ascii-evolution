import random
import string


target = "Evolutionary algorithms are fun!"
population_size = 100
mutation_rate = 0.15
generations = 1000

def generate_random_string(length: int) -> str:
    letters = string.ascii_letters + string.punctuation + " "
    return "".join(random.choice(letters) for _ in range(length))


def calculate_fitness(candidate, target) -> int:
    f = 0
    for i in range(len(target)):
        f+= abs(ord(candidate[i]) - ord(target[i]))
    return f


def create_population(population_size, target_length):
    return [generate_random_string(target_length) for _ in range(population_size)]


def tournament_selection(population) -> str:  
    random_candidates = random.sample(population, 5)
    best_candidate = min(random_candidates, key=lambda c: calculate_fitness(c, target))
    return best_candidate


def crossover(parent1, parent2) -> str:
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child


def mutate_string(candidate) -> str:
    new_candidate = ""
    for char in candidate:
        if random.random() < mutation_rate:
            new_candidate += random.choice(string.ascii_letters + string.punctuation + ' ')
        else:
            new_candidate += char
    return new_candidate
























def main():
    
    test_string = generate_random_string(len(target))
    population = create_population(
    population_size,
    len(target)
    )
    best = tournament_selection(population)
    print(target)
    print(test_string)
    print(len(test_string) == len(target))
    print(calculate_fitness(test_string, target))


    print("Population size:", len(population))
    print("Best candidate:", best)
    print("Fitness:", calculate_fitness(best, target))
    
    parent1 = population[0]
    parent2 = population[1]
    child = crossover(parent1, parent2)

    print("\nParent 1:", parent1)
    print("Parent 2:", parent2)
    print("Child:   ", child)




    mutated = mutate_string(target)

    print("Original:", target)
    print("Mutated: ", mutated)
    print("Length OK:", len(target) == len(mutated))
    print("Changed:", target != mutated)

if __name__ == "__main__":
    main()