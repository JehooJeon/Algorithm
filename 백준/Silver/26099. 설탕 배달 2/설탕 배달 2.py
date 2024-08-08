n = int(input())

if n in (4, 7):
    print(-1)
else:
    if n % 5 == 0:
        print(n // 5)
    elif (n-3) % 5 == 0:
        print((n-3) // 5 + 1)
    elif (n-6) % 5 == 0:
        print((n-6) // 5 + 2)
    elif (n-9) % 5 == 0:
        print((n-9) // 5 + 3)
    elif (n-12) % 5 == 0:
        print((n-12) // 5 + 4)
    else:
        print(-1)