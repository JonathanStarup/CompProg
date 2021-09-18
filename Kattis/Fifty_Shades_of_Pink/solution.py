from sys import stdin
lines = stdin.read().splitlines()

negative = "I must watch Star Wars with my daughter"

n = int(lines[0])
buttons = 0
for line_index in range(1, 1+n):
    color = lines[line_index].lower()
    count = color.count("rose") + color.count("pink")
    if (count > 0):
        buttons += 1

if (buttons == 0):
    print(negative)
else:
    print(buttons)