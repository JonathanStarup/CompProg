import sys
import itertools as it
from collections import deque
lines = sys.stdin.read().splitlines()

n, m = map(int, lines[0].split())
gold = list(map(int, lines[1].split()))
total_cost = 0
done = [False for _ in range(n)]
friends = [[] for _ in range(n)]
for line in it.islice(lines, 2, 2 + m):
    f1, f2 = map(int, line.split())
    friends[f1-1].append(f2-1)
    friends[f2-1].append(f1-1)
reverse_index_gold = [(j, i) for (i, j) in enumerate(gold)]

def spread(node, done, gold, friends):
    done[node] = True
    todo = deque(friends[node])
    while len(todo) != 0:
        elm = todo.popleft()
        done[elm] = True
        for f in friends[elm]:
            if not done[f]:
                todo.append(f)


    return gold[node]

for cost, index in sorted(reverse_index_gold):
    if not done[index]:
        total_cost += spread(index, done, gold, friends)
print(total_cost)