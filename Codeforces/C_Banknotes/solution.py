import sys
input = iter(sys.stdin.read().splitlines())
def iinput(): return list(map(int, next(input).split()))

T = int(next(input))

for _ in range(T):
    N, K = iinput()
    K += 1
    a = iinput()
    used_a = [0]*N
    used = 0

    for i in range(1, N):
        diff = a[i] - a[i-1]
        need = K - used
        can_get = 10**diff - 1
        if need > can_get:
            used_a[i-1] = can_get
            used += can_get
        else:
            used_a[i-1] = need
            used += need
            break
    used_a[N-1] = K - used
    asd = [(10**a[i] * used_a[i]) for i in range(N)]
    reassemble = sum(asd)
    print(reassemble)
