def main():
    while True:
        sentence = input()

        if sentence == '.':
            break

        stack = []
        balanced = True

        for s in sentence:
            if s == '(' or s == '[':
                stack.append(s)
            elif s == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    balanced = False
                    break
            elif s == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    balanced = False
                    break

        if balanced and not stack:
            print('yes')
        else:
            print('no')

if __name__ == "__main__":
    main()
