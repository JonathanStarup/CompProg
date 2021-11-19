import sys
input = iter(sys.stdin.read().splitlines())

no = -1

T = int(next(input))

for test in range(T):
    N = int(next(input))
    S = next(input)
    if "aa" in S: print(2)
    elif "aba" in S or "aca" in S: print(3)
    elif "abca" in S or "acba" in S: print(4)
    elif "abbacca" in S or "accabba" in S: print(7)
    else: print(no)