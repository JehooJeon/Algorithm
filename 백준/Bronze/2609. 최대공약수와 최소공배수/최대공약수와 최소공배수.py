N, M = map(int, input().split())

# 최대공약수
GCD = 0
if N > M:
    for i in range(1, M + 1):
        if N % i == 0 and M % i == 0:
            GCD = i
else:
    for i in range(1, N + 1):
        if N % i == 0 and M % i == 0:
            GCD = i
print(GCD)

# 최소공배수
LCM = N * (M // GCD)
print(LCM)