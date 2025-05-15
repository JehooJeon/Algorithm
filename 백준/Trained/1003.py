def main():
    T = int(input())

    for _ in range(T):
        N = int(input())
        if N == 0:
            print('1 0')
            continue

        dp = [[0, 0] for _ in range(N + 1)]
        dp[0] = [1, 0]
        dp[1] = [0, 1]

        if N >= 2:
            cnt = 2
            while cnt < N + 1:
                dp[cnt] = [i + j for i, j in zip(dp[cnt - 1], dp[cnt - 2])]
                cnt += 1

        for i in dp[N]:
            print(i, end=' ')

if __name__ == "__main__":
    main()
