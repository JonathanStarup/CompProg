from sys import stdin
lines = stdin.read().splitlines()

n = int(lines[0])
lens = [int(lines[x]) for x in range(1, n+1)]
best_max = 10000
best_len = 2*best_max + 1
best_i = -1

for i in range(n):
    cur_len = lens[i] + lens[(i+n-2) % n]
    if cur_len < best_len:
        best_len = cur_len
        best_i = i

print(best_len)