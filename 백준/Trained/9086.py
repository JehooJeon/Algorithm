def first_last_print(word):
    print(word[0] + word[-1])

def main():
    T = int(input())
    for _ in range(T):
        first_last_print(input())

if __name__ == "__main__":
    main()
