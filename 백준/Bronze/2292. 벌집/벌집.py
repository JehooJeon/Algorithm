N = int(input())

max_num = 1
cnt = 0
power = 0
while True:
    max_num += 6*power
    cnt += 1
    if N > max_num:
        power += 1
    else:
        break

print(cnt)
