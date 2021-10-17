import sys
INF = float('inf')
input = iter(sys.stdin.read().splitlines())
def iinput(): return list(map(int, next(input).split()))
def debug(*ss): print("  >"+" ".join(map(lambda s:f"{s:>8} = {globals()[s] if s in globals() else locals()[s]:<10}", ss)))
