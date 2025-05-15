def main():
    N, K = map(int, input().split())

    coin_values = [int(input()) for _ in range(N)]
    cnt = 0

    for coin in coin_values[::-1]:
        cnt += K // coin
        K = K % coin

    print(cnt)

if __name__ == "__main__":
    main()
