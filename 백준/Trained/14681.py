def solution(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    return 4

x = int(input())
y = int(input())
print(solution(x, y))
