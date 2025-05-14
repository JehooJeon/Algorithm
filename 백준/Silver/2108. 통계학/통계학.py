import sys
from collections import Counter

def mean(arr):
    return round(sum(arr) / len(arr))

def median(arr):
    arr.sort()
    if len(arr) % 2 == 0:
        return mean([arr[len(arr) // 2 - 1], arr[len(arr) // 2]])
    return arr[len(arr) // 2]

def mode(arr):
    dic = Counter(arr)
    max_value = max(dic.values())
    modes = [k for k, v in dic.items() if v == max_value]
    modes.sort()
    
    if len(modes) == 1:
        return modes[0]
    return modes[1]

def scale(arr):
    return max(arr) - min(arr)

def main():
    N = int(input())
    arr = list(int(sys.stdin.readline()) for _ in range(N))
    print(mean(arr))
    print(median(arr))
    print(mode(arr))
    print(scale(arr))

if __name__ == "__main__":
    main()
