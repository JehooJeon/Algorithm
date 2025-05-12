def solution(A, B):
    for b in B:
        A = A.replace(b, b.lower())
    return A

A = input()
B = list(input().split())
print(solution(A, B))
