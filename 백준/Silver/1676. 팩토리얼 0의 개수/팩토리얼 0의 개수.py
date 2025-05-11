N = int(input())

def zero_counter(N):
    cnt = 0
    num = 5

    while True:
        if N // num != 0:
            cnt += N // num
        else:
            break
        
        num *= 5

    return cnt

print(zero_counter(N))
