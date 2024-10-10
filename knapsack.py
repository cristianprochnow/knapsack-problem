import random

# GA

POPULATION_SIZE = 10
GENOME_SIZE = 8
MUTATION_SIZE = 0.05
GENERATIONS = 20


def fitness(element):
    return sum(element)


def build_element():
    return [random.randint(0, 1) for _ in range(GENOME_SIZE)]


def build_population():
    return [build_element() for _ in range(POPULATION_SIZE)]


def crossover(first, second):
    cut_point = random.randint(1, GENOME_SIZE - 1)
    child = first[:cut_point] + second[cut_point:]

    return child


def mutation(element):
    for index in range(GENOME_SIZE):
        if random.random() < MUTATION_SIZE:
            element[index] = 1 - element[index]

    return element


def selection(population):
    sorted_population = sorted(
        population,
        key=lambda element: fitness(element),
        reverse=True
    )

    return sorted_population[:POPULATION_SIZE // 2]


def evolve(population):
    new_population = []
    selected_parents = selection(population)

    while len(new_population) < POPULATION_SIZE:
        first = random.choice(selected_parents)
        second = random.choice(selected_parents)
        child = crossover(first, second)
        child = mutation(child)

        new_population.append(child)

    return new_population


population = build_population()
greatest = []

for generation in range(GENERATIONS):
    population = evolve(population)
    greatest = max(population, key=lambda element: fitness(element))

    print(f"Geração {generation + 1}: Melhor Aptidão = {fitness(greatest)}")

print("Melhor solução: ", greatest)
