# 找最大正方形，我是每3*3,5*5,...看每一行是否都為一樣的，再增加length，須注意測資有在四條邊上的點，這些點皆為1
# v1
t = int(input())
for i in range(t):
    m, n, q = map(int, input().split())
    print("%d %d %d" % (m, n, q))
    grid = []
    for j in range(m):
        grid.append(input())
    for j in range(q):
        r, c = map(int, input().split())
        if r == (m - 1) or c == (n - 1) or r == 0 or c == 0:
            print(1)
        else:
            fr, er = r - 1, r + 1
            fc, ec = c - 1, c + 1
            length = 1
            while True:
                count = 0
                for k in range(fr, er + 1):
                    if grid[k][fc:ec + 1] == grid[r][c] * (length + 2):
                        count += 1
                if count == (ec + 1 - fc):
                    length += 2
                    fr, er = fr - 1, er + 1
                    fc, ec = fc - 1, ec + 1
                    if fr < 0 or er < 0 or fc < 0 or ec < 0 or er >= m or ec >= n:
                        break
                else:
                    break
            print(length)

# v2
for i in range(int(input())):
    m, n, q = map(int, input().split())
    print(m, n, q)
    g = []
    for j in range(m):
        g.append(input())
    for j in range(q):
        r, c = map(int, input().split())
        pivot = g[r][c]
        count = 1
        ans = 1
        record = 0
        while 1:
            try:
                for k in range(r - count, r + count + 1):
                    if g[k][c - count:c + count + 1] != pivot * (ans + 2):
                        # print(g[k][c-count:c+count+1])
                        record = 1
                        break
                if record:
                    break
                count += 1
                ans += 2
            except:
                break
        print(ans)

# v3
for i in range(int(input())):
    m, n, q = map(int, input().split())
    print(m, n, q)
    grid = []
    for k in range(m):
        grid.append(input())
    for k in range(q):
        a, b = map(int, input().split())
        ans = 1
        record = 1
        while True:
            try:
                for j in range(a - ans, a + ans + 1):
                    for h in range(b - ans, b + ans + 1):
                        if grid[j][h] != grid[a][b] or (j < 0 or j > m or h < 0 or h > n):
                            record = 0
                            break
                    #	print(j, h)
                    if not record:
                        break
                if not record:
                    break
                else:
                    ans += 1
            except:
                break
        print(ans * 2 - 1)
