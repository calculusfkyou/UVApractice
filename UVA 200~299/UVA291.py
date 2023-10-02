edge = [[0] * 6 for _ in range(6)]


# 已繪製k條邊，將端點x加入
def dfs(x, k, s):
    s += str(x)
    if k == 8:
        print(s)
        return
    for y in range(1, 6):
        if edge[x][y]:
            edge[x][y] = edge[y][x] = 0
            dfs(y, k + 1, s)
            edge[x][y] = edge[y][x] = 1


if __name__ == "__main__":
    for i in range(1, 6):
        for j in range(1, 6):
            if i != j:
                edge[i][j] = 1
    edge[4][1] = edge[1][4] = 0  # 1、4和2、4不相連
    edge[4][2] = edge[2][4] = 0
    dfs(1, 0, "")
