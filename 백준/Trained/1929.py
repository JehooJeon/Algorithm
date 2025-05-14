def main():
    N, M = map(int, input().split())

    for i in range(N, M + 1):
        if i == 1:
            continue

        if i in [2, 3]:
            print(i)
            continue

        n = int(i ** (1 / 2))
        is_prime = True
        for j in range(2, n + 1):
            if i % j == 0:
                is_prime = False
                break
                
        if is_prime:
            print(i)

if __name__ == "__main__":
    main()
