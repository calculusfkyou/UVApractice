# 經典DFS題目，其實BFS也可以，但DFS相對直觀，練習遞迴的好題目。

directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]


def dfs(row, col):
    if row < 0 or row >= n or col < 0 or col >= m:
        return 0
    if graph[row][col] == '*':
        return 0

    graph[row][col] = '*'

    for d in directions:
        dfs(row + d[0], col + d[1])

    return 1


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    graph = []
    for i in range(n):
        graph.append(list(input()))

    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '@':
                dfs(i, j)
                count += 1

    print(count)
