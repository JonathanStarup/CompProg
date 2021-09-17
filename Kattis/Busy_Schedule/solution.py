from sys import stdin
lines = stdin.read().splitlines()
output = []

def d(s):
    time_str = s.split()
    am = time_str[1] == "a.m."
    hour, minute = map(int, time_str[0].split(":"))
    if hour == 12 and am:
        return (minute, s)
    elif am:
        return (hour*100+minute, s)
    elif hour == 12 and (not am):
        return (hour*100+minute, s)
    else:
        return ((12+hour)*100+minute, s)


line_n = 0
while 1:
    app = int(lines[line_n])
    if app == 0:
        break
    dates = [d(lines[i]) for i in range(line_n+1, line_n+1+app)] 
    dates.sort()
    output.extend(map(lambda x: x[1], dates))
    output.append("")
    line_n += app + 1

print("\n".join(output))