# https://open.kattis.com/problems/oddecho
import sys
input = iter(sys.stdin.read().splitlines())
def ii(): return int(next(input))
def iii(): return list(map(int, next(input).split()))

n = ii()
for yell_i in range(n):
    w = next(input)
    if yell_i % 2 == 0: print(w)
