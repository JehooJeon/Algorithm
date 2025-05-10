import sys

def main():
    arr = list(range(1, 31))
    for _ in range(28):
        n = int(sys.stdin.readline())
        arr.remove(n)
    for a in arr:
        print(a)

if __name__ == "__main__":
    main()