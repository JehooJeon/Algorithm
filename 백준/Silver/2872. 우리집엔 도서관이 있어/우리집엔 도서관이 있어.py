# N: 책의 개수
N = int(input())
# book_list: 책의 순서 리스트
book_list = [int(input()) for _ in range(N)]

cnt = N
for _ in range(N):
    num = book_list.pop()
    if N == num:
        N -= 1

print(N)