import sys

def solution(N):
    stack = []

    for _ in range(N):
        arr = sys.stdin.readline().split()
        if arr[0] == 'push':
            stack.append(int(arr[1]))
        elif arr[0] == 'pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif arr[0] == 'size':
            print(len(stack))
        elif arr[0] == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        elif arr[0] == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)

def main():
    N = int(input())
    solution(N)

if __name__ == "__main__":
    main()
