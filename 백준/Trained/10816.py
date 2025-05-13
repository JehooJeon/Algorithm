def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))

    cards = {int(key): 0 for key in B}

    for a in A:
        if a in cards:
            cards[a] += 1
    
    for key in B:
        print(cards[key], end=' ')

if __name__ == "__main__":
    main()
