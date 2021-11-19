import sys
INF = float('inf')
input = iter(sys.stdin.read().splitlines())
def iinput(): return list(map(int, next(input).split()))
def debug(*ss): print("  >"+" ".join(map(lambda s:f"{s:>8} = {globals()[s] if s in globals() else locals()[s]:<10}", ss)))

yes = "YES"
no = "NO"

T = int(next(input)) # <= 10**4

for test in range(T):
    N = int(next(input)) # 1 <= n <= 2*10**5
    a = iinput() # +- 10**9
    ac = next(input)
    reds, blues = [], []
    for i in range(N):
        if ac[i] == "R": reds.append(a[i])
        else: blues.append(a[i])
    reds.sort()
    blues.sort()
    blueP, redP = 0, 0

    # blue can decrement
    # red can increment

    solution = yes

    #print()
    for want in range(1, N+1):
        #print(f"for {want} i ...")
        if blueP < len(blues) and blues[blueP] >= want:
            blueP += 1
            #print(f"picked blue number {blues[blueP-1]:6d}")
        elif redP < len(reds) and reds[redP] <= want:
            redP += 1
            #print(f"picked red number {reds[redP-1]:6d}")
        else:
            solution = no
            break
    print(solution)
