import sys

def new_operator(A, B):
    return (A + B) * (A - B)

def main():
    A, B = map(int, sys.stdin.readline().split())
    print(new_operator(A, B))

if __name__ == "__main__":
    main()