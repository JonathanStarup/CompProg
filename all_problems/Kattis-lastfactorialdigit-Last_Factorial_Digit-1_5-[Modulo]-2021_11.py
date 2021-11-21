# https://open.kattis.com/problems/lastfactorialdigit
T = int(input())
for _ in range(T):
    N = int(input())
    res = 1
    for i in range(2, N+1):
        res = res * (i % 10) % 10
    print(res)