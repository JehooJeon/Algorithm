def plastic(N, dp):
    for i in range(6, N + 1):
        if dp[i - 3] != -1 and dp[i - 5] != -1:
            dp[i] = min(dp[i - 3], dp[i - 5]) + 1
        elif dp[i - 3] != -1:
            dp[i] = dp[i - 3] + 1
        elif dp[i - 5] != -1:
            dp[i] = dp[i - 5] + 1
        else:
            dp[i] = -1
    
    return dp[N]

def main():
    N = int(input())
    dp = [-1] * (N + 1)
    dp[3] = 1

    if N >= 5:
        dp[5] = 1
        print(plastic(N, dp))   
    else:
        print(dp[N])

if __name__ == "__main__":
    main()
