from collections import deque
import sys

def solution(N):
    queue = deque()

    for _ in range(N):
        order = list(sys.stdin.readline().split())
        if order[0] == 'push':
            queue.append(order[1])
        elif order[0] == 'pop':
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif order[0] == 'size':
            print(len(queue))
        elif order[0] == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        elif order[0] == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif order[0] == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)

def main():
    N = int(input())
    solution(N)

if __name__ == "__main__":
    main()
    