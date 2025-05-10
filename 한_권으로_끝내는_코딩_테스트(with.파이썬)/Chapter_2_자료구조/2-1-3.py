def solution(A, B):
    a, b = 0, 0
    for i in range(len(A)):
        if A[i] > B[i]:
            a += 1
        elif A[i] < B[i]:
            b += 1
    
    if a > b:
        return 1
    return 0

A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solution(A, B))
