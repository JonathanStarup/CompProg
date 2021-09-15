import sys

lines = sys.stdin.read().splitlines()

total_time = 0
n = int(lines[0])
timer_on = False
prev = 0

for str_time in lines[1:]:
    time = int(str_time)
    if (timer_on):
        total_time += time - prev
    timer_on = not timer_on
    prev = time
if timer_on:
    print("still running")
else:
    print(total_time)
