import sys

def main():
    N, M = map(int, input().split())
    poketmon_name = {}
    poketmon_num = {}

    for i in range(1, N + 1):
        name = sys.stdin.readline().strip()
        poketmon_name[name] = i
        poketmon_num[i] = name

    for _ in range(M):
        problem = sys.stdin.readline().strip()
        if problem.isdigit():
            print(poketmon_num[int(problem)])
        else:
            print(poketmon_name[problem])

if __name__ == "__main__":
    main()
