m = int(input())
highest_base = 75
negative = "none"

pws = [i ** 3 for i in range(highest_base+2)]
occ = {}
for a in range(1, highest_base+2):
    for b in range(a, highest_base+2):
        n = pws[a] + pws[b]
        if n <= m:
            occ[n] = occ.get(n, 0) + 1
rel = [x[0] for x in occ.items() if x[1] >= 2]
if len(rel) == 0:
    print(negative)
else:
    print(max(rel))

