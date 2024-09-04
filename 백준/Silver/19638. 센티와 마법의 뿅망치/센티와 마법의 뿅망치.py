import heapq

def main():
    # N: 센티를 제외한 거인의 나라의 인구수, H: 센티의 키, T: 마법의 뿅망치의 횟수 제한
    N, H, T = map(int, input().split())
    # heights: 각 거인의 키를 나타내는 리스트
    heights = list(-int(input()) for _ in range(N))
    # cnt: 뿅망치 사용 횟수
    cnt = 0

    heapq.heapify(heights)

    while True:
        max_height = -heapq.heappop(heights)

        # 만약 가장 키가 큰 거인의 키가 센티보다 작으면,
        # YES를 출력하고, 마법의 뿅망치를 최소로 사용한 횟수 출력
        if max_height < H:
            print('YES')
            print(cnt)
            break
        
        # 만약 가장 키가 큰 거인의 키가 센티보다 크거나 같은데,
        # 뿅망치 횟수 제한을 모두 사용한 경우
        # NO를 출력하고, 마법의 뿅망치 사용 이후 거인의 나라에서 키가 가장 큰 거인의 키 출력
        if cnt == T:
            print('NO')
            print(max_height)
            break
        
        # 가장 키가 큰 거인의 키가 1인 경우 뿅망치의 영향 X
        if max_height == 1:
            heapq.heappush(heights, -1)
            cnt += 1
            continue

        # 두 경우 모두 아닌 경우에는 뿅망치를 사용해서
        # 가장 키가 큰 거인의 키를 2로 나눠줌
        new_height = max_height // 2
        heapq.heappush(heights, -new_height)
        cnt += 1

if __name__ == '__main__':
    main()