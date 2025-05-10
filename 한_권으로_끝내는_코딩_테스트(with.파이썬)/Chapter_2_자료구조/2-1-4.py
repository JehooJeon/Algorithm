def solution(n, k, A):
    answer = 0
    
    for array in A:
        for a in array:
            if a == k:
                answer += 1

    return answer

n, k = map(int, input().split())
A = list(list(map(int, input().split()) for _ in range(n)))
print(solution(n ,k, A))
