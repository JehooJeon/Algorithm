# n, A : 크기 n인 정수형 배열 A
# 배열 A의 원소 중에서 값이 k인 원소의 개수를 출력
def solution(n, A, k):
    answer = 0

    # 배열 A의 원소 중에서 k와 같은 값이 있으면
    # answer를 1만큼 증가시킴
    for a in A:
        if a == k:
            answer += 1
    
    return answer

# 입력을 받고 정답을 출력
n, k = map(int, input().split())
A = list(map(int, input().split()))
print(solution(n, A, k))