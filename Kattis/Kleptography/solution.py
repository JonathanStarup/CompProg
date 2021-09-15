import sys

lines = sys.stdin.read().splitlines()

letters = [x for x in range(ord('a'), ord('z')+1)]
t = {chr(x): x - ord('a') for x in letters}
t_inv = {k:v for (v,k) in t.items()}

n, m = map(lambda x: int(x), lines[0].split())
last_letters = [t[x] for x in lines[1]]
cipher = [t[x] for x in lines[2]]
print(t)


mod = 26

diff = (cipher[-1] + mod - last_letters[-1]) % mod
text = [t_inv[(x + diff) % mod] for x in cipher]

inv = lambda x: t_inv[x]

print(list(map(inv, last_letters)))
print(list(map(inv, cipher)))

print("".join(text))
