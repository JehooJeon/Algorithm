# n: 카드의 개수, m: 카드 합체를 몇 번 하는지
n, m = map(int, input().split())
# cards: 카드의 상태를 나타내는 자연수 리스트
cards = list(map(int, input().split()))

for i in range(m):
    cards.sort()
    sum_cards = cards[0] + cards[1]
    cards[0] = sum_cards
    cards[1] = sum_cards

print(sum(cards))