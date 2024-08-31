def dfs(r_x, r_y, count):
    # 촌수 +1
    count += 1
    # 방문 여부 처리
    visited[r_x] = 1

    if r_x == r_y:
        result.append(count)

    for i in graph[r_x]:
        if not visited[i]:
            dfs(i, r_y, count)

# n: 전체 사람의 수
n = int(input())
# r_x, r_y: 촌수를 계산해야 하는 서로 다른 두 사람의 번호
r_x, r_y = map(int, input().split())
# m: 부모 자식들 간의 관계의 개수
m = int(input())
# graph: 부모-자식 관계 리스트
graph = [[] for _ in range(n+1)]
# visited: 방문 여부 리스트
visited = [0] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = []

dfs(r_x, r_y, 0)

if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)