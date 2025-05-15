def main():
    N = int(input())
    time = list(map(int, input().split()))
    time.sort()
    total_time = 0
    sum_time = 0

    for t in time:
        sum_time += t
        total_time += sum_time

    print(total_time)

if __name__ == "__main__":
    main()
