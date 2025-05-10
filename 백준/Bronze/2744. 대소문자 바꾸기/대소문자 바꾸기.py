import sys

def word_conversion(word):
    answer = ''

    for w in word:
        if w.isupper():
            answer += w.lower()
        else:
            answer += w.upper()
    
    return answer

def main():
    word = sys.stdin.readline()
    print(word_conversion(word))

if __name__ == "__main__":
    main()
    