import sys

def main():
    n = int(input())
    stack = []
    result = []
    cnt = 1

    for _ in range(n):
        seq = int(sys.stdin.readline())

        while cnt <= seq:
            stack.append(cnt)
            result.append('+')
            cnt += 1
        
        if stack[-1] == seq:
            stack.pop()
            result.append('-')

    if stack:
        print('NO')
    else:
        for r in result:
            print(r)

if __name__ == "__main__":
    main()
