# R: 퍼즐의 줄 개수, C: 각 줄의 개수
# 2 <= R, C <= 20
R, C = map(int, input().split())
crosswords = [list(input()) for _ in range(R)]

word_list = []
# 가로로 되어있는 단어 추출
for crossword in crosswords:
    # 단어를 만들기 위한 word 초기화
    word = ''
    idx = 0
    while True:
        if idx == C:
            break
        if crossword[idx] == '#':
            if len(word) >= 2:
                word_list.append(word)
            idx += 1
            word = ''
            continue
        word += crossword[idx]
        idx += 1
    if len(word) >= 2:
        word_list.append(word)

# 세로로 되어있는 단어 추출
# R: 4, C: 5
for i in range(C):
    word = ''
    for j in range(R):
        if crosswords[j][i] == '#':
            if len(word) >= 2:
                word_list.append(word)
            word = ''
            continue
        word += crosswords[j][i]
    if len(word) >= 2:
        word_list.append(word)

word_list.sort()
print(word_list[0])