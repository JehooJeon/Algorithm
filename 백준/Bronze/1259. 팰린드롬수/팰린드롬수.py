while True:
    N = input()
    if N == '0':
        break

    reverse = N[-1::-1]
    if N == reverse:
        print('yes')
        continue
    print('no')