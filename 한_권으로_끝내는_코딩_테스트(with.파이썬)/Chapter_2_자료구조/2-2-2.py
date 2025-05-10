def solution(A):
    B = ''

    for a in A:
        if a.islower():
            B += a

    return B

A = input()
print(solution(A))
