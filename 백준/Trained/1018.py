def basic_chess():
    chess_W = []
    chess_B = []

    for i in range(8):
        if i % 2 == 0:
            chess_W.append('WBWBWBWB')
            chess_B.append('BWBWBWBW')
        else:
            chess_W.append('BWBWBWBW')
            chess_B.append('WBWBWBWB')
    
    return chess_W, chess_B

def chess_maker(N, M, arr, chess_W, chess_B):
    cnt = 64

    for i in range(N - 7):
        for j in range(M - 7):
            cnt_W = 0
            cnt_B = 0
            for k in range(8):
                for l in range(8):
                    if arr[i + k][j + l] != chess_W[k][l]:
                        cnt_W += 1
                    if arr[i + k][j + l] != chess_B[k][l]:
                        cnt_B += 1
            cnt = min(cnt, cnt_W, cnt_B)
    
    return cnt

def main():
    N, M = map(int, input().split())
    arr = list(input() for _ in range(N))
    chess_W, chess_B = basic_chess()
    print(chess_maker(N, M, arr, chess_W, chess_B))

if __name__ == "__main__":
    main()
