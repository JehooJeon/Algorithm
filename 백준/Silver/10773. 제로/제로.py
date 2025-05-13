import sys

def zero(K):
    stack = []

    for _ in range(K):
        num = int(sys.stdin.readline())
        if num == 0:
            stack.pop()
        else:
            stack.append(num)

    return sum(stack)

def main():
    K = int(input())
    print(zero(K))

if __name__ == "__main__":
    main()
