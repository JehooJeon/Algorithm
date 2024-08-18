# N: 집의 크기 (3 <= N <= 16)
N = int(input())
# houses: 집의 상태 리스트 (0: 빈 칸, 1: 벽)
# (1, 1)과 (1, 2)는 항상 빈 칸
houses = [list(map(int, input().split())) for _ in range(N)]
# dp: 위치별로 이동시키는 방법의 개수 (오른쪽, 아래, 오른쪽 아래 대각선)
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]

# 첫 번째 행의 경우에는 오른쪽으로 이동하는 경우밖에 없음
for i in range(N):
    if houses[0][i] == 0:
        dp[0][i][0] = 1

def find_pipe(houses, dp):

    for x in range(N):
        for y in range(2, N):
            # 만약 이동하려는 위치에 벽이 있는 경우
            if houses[x][y] == 1:
                continue

            # 파이프가 가로로 움직이는 경우
            dp[x][y][0] = dp[x][y - 1][0] + dp[x][y - 1][2]

            # 파이프가 세로로 움직이는 경우
            dp[x][y][1] = dp[x-1][y][1] + dp[x-1][y][2]

            # 파이프가 대각선으로 움직이는 경우
            if houses[x-1][y] == 0 and houses[x][y-1] == 0:
                dp[x][y][2] = dp[x-1][y-1][0] + dp[x-1][y-1][1] + dp[x-1][y-1][2]

    return sum(dp[-1][-1])

result = find_pipe(houses, dp)
print(result)