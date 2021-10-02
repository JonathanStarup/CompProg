import sys
lines = sys.stdin.read().splitlines()
n, m = map(int, lines[0].split())
edges = [[] for _ in range(n)]
for line_i in range(1, 1+m):
    u, v = map(int, lines[line_i].split())
    edges[u-1].append(v-1)
    edges[v-1].append(u-1)
longest = [0 for _ in range(n)]
for index in range(n):
    longest[index] = max(map(lambda x: longest[x], filter(lambda x: x < index, edges[index])), default=-1) + 1
best_hedgehog = 0
for index in range(n):
    best_hedgehog = max(best_hedgehog, (longest[index]+1) * len(edges[index]))
print(best_hedgehog)