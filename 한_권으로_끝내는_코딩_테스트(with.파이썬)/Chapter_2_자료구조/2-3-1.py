def solution(A, B):
    dic = dict()

    for name, price in A:
        dic[name] = price

    answer = 0
    for b in B:
        answer += int(dic[b])

    return answer

try:
    n, m = map(int, input().split())
    A = list(list(input().split()) for _ in range(n))
    B = list(input().split())
    print(solution(A, B))
except ValueError:
    print("잘못된 값을 입력하셨습니다.")
