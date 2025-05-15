import sys

def main():
    N, M = map(int, input().split())
    site_password = dict()

    for _ in range(N):
        s, p = sys.stdin.readline().split()
        site_password[s] = p

    for _ in range(M):
        site = sys.stdin.readline().strip()
        print(site_password[site])

if __name__ == "__main__":
    main()
