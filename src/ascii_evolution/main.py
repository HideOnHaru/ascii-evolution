import random
import string


target = "Evolutionary algorithms are fun!"
population_size = 100
mutation_rate = 0.01
generations = 1000

pop = []

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
    random_candidates = random.sample(population, 20)
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


def evolve_population(population):
    new_population = []
    for _ in range(population_size):
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)
        child = crossover(parent1, parent2)
        child = mutate_string(child)
        new_population.append(child)
    return new_population




def run(): 
    pop = create_population(population_size, len(target))
    for _ in range(generations):
       pop =evolve_population(pop)
       best_candidate = min(pop, key=lambda c: calculate_fitness(c, target))
       print(f"Best candidate: {best_candidate} with fitness: {calculate_fitness(best_candidate, target)}")
       print(f"Current mutation rate: {mutation_rate}")
       print (f"greneration: {_}")
       if best_candidate == target:
           print("Target string found!")
           break    



















def main():
    run()
    

if __name__ == "__main__":
    main()