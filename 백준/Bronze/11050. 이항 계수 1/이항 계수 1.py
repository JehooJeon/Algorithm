N, K = map(int, input().split())
from math import factorial

answer = factorial(N) / (factorial(K) * factorial(N-K))

print(int(answer))