N = int(input())

arr = [int(input()) for _ in range(N)]
arr.sort()

for result in arr:
    print(result)