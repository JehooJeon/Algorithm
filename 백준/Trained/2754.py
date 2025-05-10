def score_calculation(score):
    
    if len(score) == 1:
        return 0.0
    
    if score[0] == 'A':
        answer = 4.0
    elif score[0] == 'B':
        answer = 3.0
    elif score[0] == 'C':
        answer = 2.0
    elif score[0] == 'D':
        answer = 1.0
    
    if score[1] == '+':
        return answer + 0.3
    elif score[1] == '0':
        return answer
    elif score[1] == '-':
        return answer - 0.3

score = input()
print(score_calculation(score))
