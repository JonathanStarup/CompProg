from sys import stdin
import itertools as it
lines = stdin.read().splitlines()
neg = "NO"
pos = "YES"

n, s = map(int, lines[0].split())
forwards = list(map(lambda x: x == "1", lines[1].split()))
backwards = list(map(lambda x: x == "1", lines[2].split()))
if not forwards[0]:
    print(neg)
elif forwards[s-1]:
    print(pos)
elif not backwards[s-1]:
    print(neg)
else:
    for stop in range(s, n):
        if forwards[stop] and backwards[stop]:
            print(pos)
            exit()
    print(neg)
    

