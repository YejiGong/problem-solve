import sys
input = sys.stdin.readline
n = int(input())

mos_enter_exit = {}

for _ in range(n):
    enter, exit_ = map(int, input().split())

    mos_enter_exit[enter] = mos_enter_exit.get(enter, 0) + 1
    mos_enter_exit[exit_] = mos_enter_exit.get(exit_, 0) - 1

max_mos_count = -1
max_mos_time = [None, None]

check = False

mos = sorted(mos_enter_exit.keys())
sum_mos = 0


for time in mos:
    sum_mos += mos_enter_exit[time]

    if sum_mos > max_mos_count:
        max_mos_count = sum_mos
        max_mos_time[0] = time
        check = True

    elif sum_mos < max_mos_count and check:
        max_mos_time[1] = time
        check = False

print(max_mos_count)
print(max_mos_time[0], max_mos_time[1])