import sys

def main():
    N, M = map(int, input().split())

    unheard_names = set([sys.stdin.readline().strip() for _ in range(N)])
    unseen_names = set([sys.stdin.readline().strip() for _ in range(M)])
    
    result = sorted(unheard_names & unseen_names)

    print(len(result))
    print('\n'.join(result))

if __name__ == "__main__":
    main()
