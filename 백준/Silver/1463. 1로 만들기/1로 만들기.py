def dp(N):
    if N == 1:
        return 0
    
    if N <= 3:
        return 1
    
    arr = [0] * (N + 1)
    arr[2], arr[3] = 1, 1

    idx = 4
    while idx <= N:
        if idx % 3 == 0 and idx % 2 == 0:
            arr[idx] = min(arr[idx - 1], arr[idx // 2], arr[idx // 3]) + 1
        elif idx % 3 == 0:
            arr[idx] = min(arr[idx - 1], arr[idx // 3]) + 1
        elif idx % 2 == 0:
            arr[idx] = min(arr[idx - 1], arr[idx // 2]) + 1
        else:
            arr[idx] = arr[idx - 1] + 1
        idx += 1

    return arr[N]

def main():
    N = int(input())
    print(dp(N))
    
if __name__ == "__main__":
    main()
