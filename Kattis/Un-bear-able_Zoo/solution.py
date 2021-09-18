from sys import stdin
lines = stdin.read().splitlines()
output = []

line_index = 0
test_n = 1

while 1:
    n = int(lines[line_index])
    line_index += 1
    if n == 0:
        break

    animals = {}
    for animal_index in range(line_index, line_index + n):
        animal = lines[animal_index].split()[-1].lower()
        animals[animal] = animals.get(animal, 0) + 1
    
    output.append(f'List {test_n}:')
    items = list(animals.items())
    items.sort()
    for animal_t in items:
        animal, count = animal_t
        output.append(f'{animal} | {count}')

    line_index += n
    test_n += 1

print("\n".join(output))