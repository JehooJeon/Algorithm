def main():
    N = int(input())
    arr = list(list(input().split()) for _ in range(N))
    arr.sort(key=lambda x: int(x[0]))

    for a in arr:
        print(a[0], a[1])
    
if __name__ == "__main__":
    main()
