from sys import stdin
lines = stdin.read().splitlines()

letters = list(range(ord('a'), ord('z')+1))
num = {chr(x): x - ord('a') for x in letters}
letter = {k:v for (v,k) in num.items()}

n, m = map(int, lines[0].split())
hint = [num[x] for x in lines[1]]
cipher = [num[x] for x in lines[2]]

plain_text = [0 for _ in range(m-n)] + hint

mod = 26

for i in range(m-n-1, -1, -1):
    plain_text[i] = (cipher[i+n] - plain_text[i+n] + mod) % mod

print("".join([letter[x] for x in plain_text]))

