# N: 카드의 개수, M: 목표 숫자
N, M = map(int, input().split())
# cards: 주어진 카드의 숫자 리스트
cards = list(map(int, input().split()))

card_sums = []
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            card_sum = cards[i] + cards[j] + cards[k]
            if card_sum <= M:
                card_sums.append(card_sum)
            else:
                continue

print(max(card_sums))