from sys import stdin
lines = stdin.read().splitlines()

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
        current = animals[animal] if animal in animals else 0
        animals[animal] = current + 1
    
    print(f'List {test_n}:')
    items = list(animals.items())
    items.sort()
    for animal_t in items:
        animal, count = animal_t
        print(f'{animal} | {count}')

    line_index += n
    test_n += 1
