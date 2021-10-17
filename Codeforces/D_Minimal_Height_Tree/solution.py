import sys
from collections import deque
#INF = float('inf')
input = iter(sys.stdin.read().splitlines())
def iinput(): return list(map(int, next(input).split()))
#def debug(*ss): print("  >"+" ".join(map(lambda s:f"{s:>8} = {globals()[s] if s in globals() else locals()[s]:<10}", ss)))

T = int(next(input))
for _ in range(T):
    N = int(next(input))
    bfs = list(iinput())
    parents = deque([0])
    group_size = 0
    reset = True
    for i in range(1, N):
        if reset:
            reset = False
            group_size += 1
            continue
        if bfs[i] < bfs[i-1]:
            reset = True
            level = parents.popleft() + 1
            parents.extend([level]*group_size)
            group_size = 0


    print(height)