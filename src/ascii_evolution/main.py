import random
import string


target = "Evolutionary algorithms are fun!"
population_size = 100
mutation_rate = 0.01
generations = 1000

def generate_random_string(length: int) -> str:
    letters = string.ascii_letters + string.punctuation + " "
    return "".join(random.choice(letters) for _ in range(length))


def calculate_fitness(candidate, target):
    f = 0
    for i in range(len(target)):
        f+= abs(ord(candidate[i]) - ord(target[i]))
    return f




























def main():
    test_string = generate_random_string(len(target))

    print(target)
    print(test_string)
    print(len(test_string) == len(target))
    print(calculate_fitness(test_string, target))


if __name__ == "__main__":
    main()