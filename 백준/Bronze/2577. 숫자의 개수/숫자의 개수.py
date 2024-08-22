A = input()
B = input()
C = input()

nums = str(int(A) * int(B) * int(C))
arr = [0] * 10

for i in nums:
    arr[int(i)] += 1

for j in arr:
    print(j)