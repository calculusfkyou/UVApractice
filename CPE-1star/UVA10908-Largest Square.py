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