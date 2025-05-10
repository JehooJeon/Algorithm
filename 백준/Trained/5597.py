import sys

def find_missing_number():
    arr = list(range(1, 31))
    
    for _ in range(28):
        n = int(sys.stdin.readline())
        arr.remove(n)
    
    print(min(arr))
    print(max(arr))

def main():
    find_missing_number()

if __name__ == "__main__":
    main()
