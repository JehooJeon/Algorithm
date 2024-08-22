T = int(input())

for _ in range(T):
    # H: 호텔의 층 수, W: 각 층의 방 수, N: 몇 번째 손님인지
    H, W, N = map(int, input().split())

    if N % H == 0:
        Y = H
        X = N // H
    else:
        Y = N % H
        X = N // H + 1
    print(Y*100 + X)