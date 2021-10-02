import sys
lines = sys.stdin.read().splitlines()
n, m = map(int, lines[0].split())
cat_location = list(map(int, lines[1].split()))
edges = [[] for _ in range(n)]
cats = [-1 for _ in range(n)]
for line_i in range(2, 2+n-1):
    x, y = map(int, lines[line_i].split())
    edges[x-1].append(y-1)
    edges[y-1].append(x-1)

start = 0
cats[start] = cat_location[start]
todo = [(e, cats[start]) for e in edges[start]]
resturants = 0
while todo:
    node, prev = todo.pop()
    cats[node] = prev + 1 if cat_location[node] == 1 else 0
    if cats[node] <= m:
        new_places = list(filter(lambda x: cats[x] == -1, edges[node]))
        if not new_places:
            #leaf
            resturants += 1
        else:
            todo.extend([(e, cats[node]) for e in new_places])
print(resturants)