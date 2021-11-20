import sys
from heapq import heappush as hpush, heappop as hpop, heapify
input = iter(sys.stdin.read().splitlines())
def iinput(): return list(map(int, next(input).split()))
output = []

T = int(next(input))

for test in range(T):
    N = int(next(input))
    a = iinput()
    heap = [(-a[i], i+1) for i in range(N)]
    heapify(heap)
    tmp_output = []
    while True:
        p1, p2 = hpop(heap), hpop(heap)
        if p1[0] == 0 or p2[0] == 0: break
        tmp_output.append(f"{p1[1]} {p2[1]}\n")
        hpush(heap, (p1[0]+1, p1[1]))
        hpush(heap, (p2[0]+1, p2[1]))
    output.append(f"{len(tmp_output)}\n")
    output.extend(f'{"".join(tmp_output)}')

print("".join(output))