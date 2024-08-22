T = int(input())

for _ in range(T):
    string = input()

    total = 0
    score = 0

    for str in string:
        if str == 'O':
            score += 1
            total += score
        elif str == 'X':
            score = 0
    
    print(total)