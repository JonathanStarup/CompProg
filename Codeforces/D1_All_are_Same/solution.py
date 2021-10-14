from sys import stdin
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
lines = stdin.read().splitlines()
tests = int(lines[0])
for test in range(tests):
    ii = test*2+1
    n = int(lines[ii])
    arr = list(map(int, lines[ii+1].split()))
    diffs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            diffs.append(abs(arr[i] - arr[j]))
    total_gcd = 0
    for diff in diffs:
        total_gcd = gcd(total_gcd, diff)
    if total_gcd == 0:
        print(-1)
    else:
        print(total_gcd)
    