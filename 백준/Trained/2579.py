def dp(N, stairs):
    score = [0] * (N + 1)

    for i in range(1, N + 1):
        if i in [1, 2]:
            score[i] = stairs[i]
            continue
        
        


def main()
    N = int(input())
    stairs = list(int(input()) for _ in range(N))
    print(dp(N, stairs))

if __name__ == "__main__":
    main()
