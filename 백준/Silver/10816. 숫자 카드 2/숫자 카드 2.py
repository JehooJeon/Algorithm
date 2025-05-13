from collections import Counter

def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    
    counter = Counter(A)
    
    for b in B:
        print(counter[b], end=' ')

if __name__ == "__main__":
    main()
