def dp(N):
    arr = [0] * (N + 1)

    for i in range(2, N + 1):
        arr[i] = arr[i - 1] + 1
        if i % 2 == 0:
            arr[i] = min(arr[i], arr[i // 2] + 1)
        if i % 3 == 0:
            arr[i] = min(arr[i], arr[i // 3] + 1)        

    return arr[N]

def main():
    N = int(input())
    print(dp(N))
    
if __name__ == "__main__":
    main()
