# https://open.kattis.com/problems/proofs
yes = "correct"
n = int(input())
facts = set()
for line in range(1, n+1):
    ass, con = [s.split() for s in input().split("->")]
    if all([a in facts for a in ass]):
        facts.update(con)
    else:
        print(line)
        exit()
print(yes)
