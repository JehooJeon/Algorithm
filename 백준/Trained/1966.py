from collections import deque

def printer_queue(M, document):
    queue = deque([(i, p) for i, p in enumerate(document)])
    cnt = 0

    while queue:
        if queue[0][1] == max(p for _, p in queue):
            idx, _ = queue.popleft()
            if idx == M:
                cnt += 1
                break
            cnt += 1
        else:
            queue.rotate(-1)
    
    return cnt

def main():

    T = int(input())

    for _ in range(T):
        N, M = map(int, input().split())
        document = map(int, input().split())
        print(printer_queue(M, document))

if __name__ == "__main__":
    main()
