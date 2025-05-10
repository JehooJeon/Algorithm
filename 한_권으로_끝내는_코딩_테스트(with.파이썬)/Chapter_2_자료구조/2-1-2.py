def solution(n, A, i, j, k):
    for idx in range(i, j + 1):
        A[idx] *= k
    
    return sum(A)

n = int(input())
A = list(map(int, input().split()))
i, j, k = map(int, input().split())
print(solution(n, A, i, j ,k))