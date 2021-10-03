import sys
lines = sys.stdin.read().splitlines()
output = []

tests = int(lines[0])
line_start = 1
test = 0
while test < tests:
    n = int(lines[line_start])
    req = [ list(map(lambda x: int(line[x])-1, range(1, len(line)))) for line in [lines[i].split() for i in range(line_start+1, line_start+1+n)]]
    print(n, req)

    # IDEA verifeid: Dag -> dp forward with req. readthroughs

    line_start += 1+n
    test += 1


print("\n".join(map(str, output)))