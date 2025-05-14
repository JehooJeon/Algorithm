import sys

def main():
    n = int(input())
    desired = list(sys.stdin.readline() for _ in range(n))
    stack = []
    start = 1

    for d in desired:
        if start == n + 1:
            break
        
        if start == d:
            stack

if __name__ == "__main__":
    main()