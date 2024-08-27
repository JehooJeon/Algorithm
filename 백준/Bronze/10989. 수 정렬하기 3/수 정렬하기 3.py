import sys

def input():
    return sys.stdin.readline()

N = int(input())

counts = [0] * 10001

for _ in range(N):
    idx = int(input())
    counts[idx] += 1

for i in range(10001):
    if counts[i] != 0:
        for _ in range(counts[i]):
            print(i)