def main():
    N = int(input())
    arr = list(list(map(int, input().split())) for _ in range(N))
    arr.sort(key=lambda x: x)

    for a in arr:
        print(a[0], a[1])

if __name__ == "__main__":
    main()
