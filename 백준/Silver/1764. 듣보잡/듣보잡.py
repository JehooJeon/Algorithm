import sys

def main():
    N, M = map(int, input().split())

    unheard_names = set([sys.stdin.readline().strip() for _ in range(N)])
    unseen_names = set([sys.stdin.readline().strip() for _ in range(M)])
    result = []

    for name in unheard_names:
        if name in unseen_names:
            result.append(name)

    result.sort()
    print(len(result))
    for r in result:
        print(r)

if __name__ == "__main__":
    main()
