N = int(input())
score = list(map(int, input().split()))

M = max(score)

result = 0
for i in range(N):
    result += score[i] / M * 100 / N

print(round(result, 6))