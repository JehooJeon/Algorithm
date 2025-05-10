# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성
def solution(N, array, v):
    answer = 0

    for a in array:
        if a == v:
            answer += 1

    return answer

N = int(input())
array = list(map(int, input().split()))
v = int(input())
print(solution(N, array, v))