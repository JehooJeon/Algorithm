import sys

def my_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    return int(num)

def main():
    n = int(input())
    opinion = list(int(sys.stdin.readline()) for _ in range(n))

    if n == 0:
        print(0)
        return

    avg = my_round(n * 0.15)

    opinion.sort()
    opinion = opinion[avg:n - avg]
    if opinion:
        print(my_round(sum(opinion) / len(opinion)))
    else:
        print(0)

if __name__ == "__main__":
    main()
