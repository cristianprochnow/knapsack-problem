import random

# GA
POPULATION_SIZE = 10
GENOME_SIZE = 8
MUTATION_SIZE = 0.1
GENERATIONS = 20
BACKPACK_SIZE = 15

# (weight, value)[]
items_for_backpack = [(2, 3), (3, 4), (4, 5), (5, 8), (9, 10), (4, 7), (2, 6), (1, 2)]
items_inserted = []

def fitness(element):
    total_value = 0
    total_weight = 0

    for index, selected in enumerate(element):
        if selected == 1:
            total_value += items_for_backpack[index][1]
            total_weight += items_for_backpack[index][0]

    if total_weight > BACKPACK_SIZE:
        return 0

    return total_value

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
has_repeated_items = False

for item in items_for_backpack:
    if (item[0], item[1]) in items_inserted:
        has_repeated_items = True
        break
    else:
        items_inserted.append((item[0], item[1]))

if has_repeated_items:
    print(f"As opções para a mochila têm de ser únicas.")
else:
    for generation in range(GENERATIONS):
        population = evolve(population)
        greatest = max(population, key=lambda element: fitness(element))

        print(f"Geração {generation + 1}: Melhor Aptidão = {fitness(greatest)}")

    print("Melhor Solução: ", greatest)
