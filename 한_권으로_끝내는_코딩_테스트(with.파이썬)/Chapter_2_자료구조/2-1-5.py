def solution(n, A, i1, j1, i2, j2, k):
    for i in range(i1, i2 + 1):
        for j in range(j1, j2 + 1):
            A[i][j] *= k

    answer = 0
    for arr in A:
        answer += sum(arr)

    return answer

n = int(input())
A = list(list(map(int, input().split())) for _ in range(n))
i1, j1, i2, j2, k = map(int, input().split())
print(solution(n, A, i1, j1, i2, j2, k))
