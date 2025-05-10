import sys

def matrix_sum():
    N, M = map(int, sys.stdin.readline().split())
    A = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
    B = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
    for i in range(N):
        for j in range(M):
            print(A[i][j] + B[i][j], end=' ')
        if i != N - 1:
            print()

def main():
    matrix_sum()

if __name__ == "__main__":
    main()
