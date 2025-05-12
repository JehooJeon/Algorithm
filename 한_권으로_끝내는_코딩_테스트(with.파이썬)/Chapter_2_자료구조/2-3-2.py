def solution(S):
    student_info = {}

    for s in S.split():
        if s in student_info:
            student_info[s] += 1
        else:
            student_info[s] = 1

    answer = list(student_info.items())
    answer.sort(key = lambda x: x[0])

    return answer

S = input()
answer = solution(S)
for name, cnt in answer:
    print(f"{name} {cnt}")
