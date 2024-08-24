# N: 참가자의 수
N = int(input())
# shirt_sizes: 티셔츠 사이즈별 신청자의 수
shirt_sizes = list(map(int, input().split()))
# T: 티셔츠 묶음 수, P: 펜 묶음 수
T, P = map(int, input().split())

shirt_cnt = 0
for size in shirt_sizes:
    if size % T == 0:
        shirt_cnt += size // T
    else:
        shirt_cnt += size // T + 1
print(shirt_cnt)

pens_cnt = N // P
pen_cnt = N % P
print(pens_cnt, pen_cnt)