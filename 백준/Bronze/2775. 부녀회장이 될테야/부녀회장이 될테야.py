T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    arr = [[0] * 15 for _ in range(15)]

    for i in range(1, 15):
        arr[0][i] = i

    for i in range(1, 15):
        for j in range(1, 15):
            if j == 1:
                arr[i][j] = 1
                continue
            arr[i][j] = arr[i-1][j] + arr[i][j-1]

    print(arr[k][n])