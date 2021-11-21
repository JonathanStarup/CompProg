# https://open.kattis.com/problems/electricaloutlets
import sys
input = iter(sys.stdin.read().splitlines())
def ii(): return int(next(input))
def iii(): return list(map(int, next(input).split()))

n = ii()
for _ in range(n):
    k_s, o_s = next(input).split(maxsplit=1)
    k = int(k_s)
    o = list(map(int, o_s.split()))
    res = o[0]
    for i in range(1, k):
        res += o[i] - 1
    print(res)
