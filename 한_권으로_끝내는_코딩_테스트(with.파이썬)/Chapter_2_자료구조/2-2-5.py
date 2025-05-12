def solution(A):
    hour = 0
    min = 0
    for a in A:
        h, m = a.split(sep=':')
        hour += int(h)
        min += int(m)
    if hour + min // 60 < 100:
        return str(f"{hour + min // 60:02d}:{min % 60:02d}")
    return str(f"{hour + min}:{min % 60:02d}")

A = list(input().split())
print(solution(A))
