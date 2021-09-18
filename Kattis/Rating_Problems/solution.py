import sys
lines = sys.stdin.read().splitlines()
n, k = [int(s) for s in lines[0].split()]

total = 0

for line_index in range(1, 1 + k):
    score = int(lines[line_index])
    total += score

missing_votes = n - k
best_case = missing_votes * 3
worst_case = missing_votes * (-3)

worst_avg = (total + worst_case) / n
best_avg = (total + best_case) / n

print(worst_avg, best_avg)

