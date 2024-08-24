N = int(input())
num_list = list(map(int, input().split()))
arr = [0] * N

for i in range(N):
    if num_list[i] == 1:
        continue
    elif num_list[i] in (2, 3):
        arr[i] = 1
    else:
        for j in range(2, int(num_list[i]**(1/2)+1)):
            if num_list[i] % j == 0:
                arr[i] = 0
                break
            else:
                arr[i] = 1
                continue

print(sum(arr))  
