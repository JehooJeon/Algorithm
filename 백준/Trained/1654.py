import sys

def lan_line_cut(K, lan_lines):
    left = 1
    right = max(lan_lines)
    max_len = 0

    while left <= right:
        mid = (left + right) // 2
        cnt = sum(lan // mid for lan in lan_lines)

        if cnt >= K:
            max_len = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return max_len

def main():
    N, K = map(int, input().split())
    lan_lines = [int(sys.stdin.readline()) for _ in range(N)]
    print(lan_line_cut(K, lan_lines))

if __name__ == "__main__":
    main()
