from collections import deque

def printer_queue(N, M):
    queue = deque(map(int, input().split()))
    idx = M
    cnt = 0

    while True:
        max_value = max(queue)

        if queue[0] == max_value:
            if idx == 0:
                cnt += 1
                break
            queue.popleft()
            cnt += 1
            idx -= 1
        else:
            queue.rotate(-1)
            if idx == 0:
                idx = len(queue) - 1
            else:
                idx -= 1
    
    return cnt

def main():

    T = int(input())

    for _ in range(T):
        N, M = map(int, input().split())
        print(printer_queue(N, M))

if __name__ == "__main__":
    main()
