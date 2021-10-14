import sys
INF = float('inf')
input = lambda: sys.stdin.readline().rstrip()
def iinput(): return list(map(int, input().split()))
def debug(*ss): print("\n".join(map(lambda s:f"\t{s} = {globals()[s] if s in globals() else locals()[s]}", ss)))


NEG = "Impossible"
N_names = int(input())
def lti(l): return ord(l) - ord('a')
def itl(i): return chr(i + ord('a'))
N = lti('z')+1
edges = [[] for _ in range(N)]
indeg = [0]*N
names = []
for _ in range(N_names):
    name = input()
    for prev_name in names:
        hit = False
        for i in range(min(len(name), len(prev_name))):
            if name[i] != prev_name[i]:
                edges[lti(prev_name[i])].append(lti(name[i]))
                indeg[lti(name[i])] += 1
                hit = True
                break
        if not hit:
            if len(name) < len(prev_name):
                print(NEG)
                exit()
    names.append(name)


todo = [i for i in range(N) if indeg[i] == 0]
if not todo:
    print(NEG)
    exit()
topsort = []
while todo:
    v1 = todo.pop()
    topsort.append(v1)
    for v2 in edges[v1]:
        indeg[v2] -= 1
        if indeg[v2] == 0:
            todo.append(v2)
if len(topsort) != N:
    print(NEG)
    exit()
print("".join(map(itl, topsort)))

    
