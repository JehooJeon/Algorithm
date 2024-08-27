arr = []

for _ in range(3):
    string = input()
    if string.isnumeric() == True:
        arr.append(int(string))
    else:
        arr.append(0)

answer = 0
for i in range(3):
    if arr[i] != 0:
        answer = arr[i] + (3 - i)

if answer % 15 == 0:
    print("FizzBuzz")
elif answer % 5 == 0:
    print("Buzz")
elif answer % 3 == 0:
    print("Fizz")
else:
    print(answer)