num_list = list(map(int, input().split()))

cnt = 0

for i in range(7):
    if num_list[i] < num_list[i+1]:
        cnt += 1
    else:
        cnt -= 1

if cnt == 7:
    print('ascending')
elif cnt == -7:
    print('descending')
else:
    print('mixed')