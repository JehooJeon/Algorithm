import sys

def end_number(N):
    cnt = 0
    num = 666

    while True:
        if '666' in str(num):
            cnt += 1
        
        if cnt == N:
            break

        num += 1
    
    return num

def main():
    N = int(sys.stdin.readline())
    print(end_number(N))

if __name__ == "__main__":
    main()
    