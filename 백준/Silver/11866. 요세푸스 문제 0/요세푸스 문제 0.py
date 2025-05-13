from collections import deque

def josephus_permutation(N, K):
    queue = deque(str(i) for i in range(1, N + 1))
    josephus = []

    for i in range(N):
        queue.rotate(-(K - 1))
        josephus.append(queue.popleft())
    
    return josephus

def main():
    N, K = map(int, input().split())
    print('<' + ', '.join(josephus_permutation(N, K)) + '>')

if __name__ == "__main__":
    main()
