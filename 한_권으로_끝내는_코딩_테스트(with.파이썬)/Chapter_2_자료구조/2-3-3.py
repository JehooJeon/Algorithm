A = list(input().split())
B = list(input().split())

student_list = {}
for a in A:
    student_list[a] = 0

for b in B:
    if b in A:
        student_list[b] += 1

for name, cnt in student_list.items():
    if cnt == 0:
        print(name)
        