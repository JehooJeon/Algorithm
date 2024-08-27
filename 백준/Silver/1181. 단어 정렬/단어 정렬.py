N = int(input())

arr = []
for _ in range(N):
    word = input()
    if (len(word), word) in arr:
        continue
    arr.append((len(word), word))

arr.sort()
for answer in arr:
    print(answer[1])