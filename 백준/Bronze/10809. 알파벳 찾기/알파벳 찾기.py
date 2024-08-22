S = input()

arr = [-1] * 26

cnt = 0
for alphabet in S:
    if arr[ord(alphabet) - 97] == -1:
        arr[ord(alphabet) - 97] = cnt
    cnt += 1

for i in arr:
    print(i, end=' ')