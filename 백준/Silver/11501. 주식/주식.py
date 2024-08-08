T = int(input())

for _ in range(T):
    # N: 날의 수 (2 <= N <= 1,000,000)
    N = int(input())
    # stock: 날 별 주가 (<= 10,000)
    stock = list(map(int, input().split()))

    # 최대 이익 초기화
    result = 0
    # 뒤에서부터 시작하면서 최댓값으로 설정
    max_price = stock.pop()

    while True:
        # 만약 남은 stock이 없을경우 정지
        if not stock:
            break

        # 만약 앞에 있는 값이 가격이 더 낮을경우 차익실현
        if max_price > stock[-1]:
            result += max_price - stock[-1]
            stock.pop()
        # 만약 앞에 있는 값이 가격이 더 높거나 같을경우 max_price 갱신
        else:
            max_price = stock.pop()

    print(result)