# N, A : 정수 N개로 이루어진 수열 A
# X : 정수
# A에서 X보다 작은 수를 모두 출력
def solution(N, X, A):
    for a in A:
        if a < X:
            print(a, end=' ')
    return       

N, X = map(int, input().split())
A = list(map(int, input().split()))
solution(N, X, A)