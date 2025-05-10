import sys

def matrix_sum():
    N, M = map(int, sys.stdin.readline().split())
    A = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
    B = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
    for i in range(N):
        result = []
        for j in range(M):
            result.append(str(A[i][j] + B[i][j]))
        print(' '.join(result))

def main():
    matrix_sum()

if __name__ == "__main__":
    main()
