N = input()
result = 0

min_num = int(N) - 9*len(N)
for i in range(min_num, int(N)):
    if i <= 0:
        continue
    create_num = i
    for j in range(len(str(i))):
        create_num += int(str(i)[j])
    if create_num == int(N):
        result = i
        break

print(result)