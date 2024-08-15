def main():
    # N: 회의의 수 (1 <= N <= 100,000)
    N = int(input())
    # meeting: 시작 시간, 끝나는 시간 리스트
    meeting = [list(map(int, input().split())) for _ in range(N)]

    # 끝나는 시간 오름차순 정렬 -> 시작 시간 오름차순 정렬
    meeting.sort(key=lambda x: (x[1], x[0]))
    # print(meeting)

    end_point = 0
    cnt = 0
    for start, end in meeting:
        if start >= end_point:
            cnt += 1
            end_point = end

    print(cnt)

if __name__ == "__main__":
    main()