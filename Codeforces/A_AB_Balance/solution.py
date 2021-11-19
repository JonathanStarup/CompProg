import sys
#INF = float('inf')
input = iter(sys.stdin.read().splitlines())
#def iinput(): return list(map(int, next(input).split()))
#def debug(*ss): print("  >"+" ".join(map(lambda s:f"{s:>8} = {globals()[s] if s in globals() else locals()[s]:<10}", ss)))

TEST = int(next(input))
for _ in range(TEST):
    S = next(input)
    n = len(S)
    if S[0] == S[n-1]:
        print(S)
        continue
    new_first = "a" if S[0] == "b" else "b"
    print(new_first + S[1:])
