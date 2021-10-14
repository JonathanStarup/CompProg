import sys
lines = sys.stdin.read().splitlines()
tests = int(lines[0])
for test_s in range(0, tests):
    ii = test_s*2+1
    n, k = map(int, lines[ii].split())
    mice = list(map(lambda x: n - int(x), lines[ii+1].split()))
    mice.sort()
    sum = 0
    count = 0
    for mouse in mice:
        if sum + mouse < n:
            sum += mouse
            count += 1
        else:
            break
    print(count)
    