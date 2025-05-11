def zero_counter(N):
    cnt = 0

    while True:
        if N // 5 != 0:
            cnt += N // 5
        else:
            break
        N //= 5

    return cnt

def main():
    N = int(input())
    print(zero_counter(N))

if __name__ == "__main__":
    main()
