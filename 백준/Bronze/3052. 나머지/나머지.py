arr = [0] * 42

for _ in range(10):
    N = int(input())
    arr[N % 42] = 1

print(sum(arr))