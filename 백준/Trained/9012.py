def main():
    T = int(input())

    for _ in range(T):
        ps = input()
        stack = []

        for p in ps:
            if p == '(':
                stack.append(p)
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(p)

        if not stack:
            print('YES')
        else:
            print('NO')

if __name__ == "__main__":
    main()
