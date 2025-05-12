def bigger_rank(arr):
    for x, y in arr:
        rank = 1
        for p, q in arr:
            if x < p and y < q:
                rank += 1
        print(rank, end=' ')

def main():
    N = int(input())
    info = list(list(map(int, input().split())) for _ in range(N))
    bigger_rank(info)

if __name__ == "__main__":
    main()
