t = int(input())
for test in range(t):
    a, b, c = map(int, input().split())
    most = max(a, b, c)
    ao = 0
    if (a == most and b == most) or (b == most and c == most) or (a == most and c == most):
        ao = 1
    out = []
    if a < most:
        print(most-a+1, end=" ")
    else:
        print(0+ao, end=" ")
    if b < most:
        print(most-b+1, end=" ")
    else:
        print(0+ao, end=" ")
    if c < most:
        print(most-c+1)
    else:
        print(0+ao)