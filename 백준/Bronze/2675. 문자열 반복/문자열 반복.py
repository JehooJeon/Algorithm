T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    P = ''

    for i in S:
        P += i*R
    
    print(P)