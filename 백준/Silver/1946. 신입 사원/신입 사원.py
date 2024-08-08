T = int(input())

for _ in range(T):
    # N: 지원자의 숫자(1 <= N <= 100,000)
    N = int(input())

    arr = [0] * N

    for _ in range(N):
        i, j = map(int, input().split())
        arr[i-1] = j

    max_score = arr[0]
    result = 1
    for i in range(1, N):
        if arr[i] < max_score:
            result += 1
            max_score = arr[i]

    print(result)