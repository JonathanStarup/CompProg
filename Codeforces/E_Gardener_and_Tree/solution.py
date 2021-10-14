from sys import stdin
from collections import deque
lines = stdin.read().splitlines()
tests = int(lines[0])
l_index = 2
for test in range(tests):
    n, k = map(int, lines[l_index].split())
    l_index += 1
    edges = [[] for _ in range(n)]
    edgen = [0 for _ in range(n)]
    for li in range(n-1):
        u, v = map(int, lines[l_index + li].split())
        edges[u-1].append(v-1)
        edges[v-1].append(u-1)
        edgen[u-1] += 1
        edgen[v-1] += 1
    l_index += n-1
    l_index += 1

    todo = deque()
    todo_next = deque()
    edges_left = n
    for v in range(n):
        if edgen[v] <= 1:
            todo.appendleft(v)
    for cut in range(k):
        while len(todo) != 0:
            next = todo.pop()
            edges_left -= 1
            for edge in edges[next]:
                if edgen[edge] > 0:
                    edgen[edge] -= 1
                if edgen[edge] == 1:
                    todo_next.appendleft(edge)
        todo, todo_next = todo_next, todo
        if len(todo) == 0:
            break
    print(edges_left)





