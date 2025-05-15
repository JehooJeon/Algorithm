def main():
    T = int(input())

    for _ in range(T):
        N = int(input())
        if N == 0:
            print('1 0')
            continue

        arr = [[0, 0]] * (N + 1)
        arr[0] = [1, 0]
        arr[1] = [0, 1]

        if N >= 2:
            cnt = 2
            while cnt < N + 1:
                arr[cnt] = [i + j for i, j in zip(arr[cnt - 1], arr[cnt - 2])]
                cnt += 1

        for i in arr[N]:
            print(i, end=' ')

if __name__ == "__main__":
    main()
