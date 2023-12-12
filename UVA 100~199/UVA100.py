# runtime error
# python直接做一定超時
while True:
    try:
        n, m = map(int, input().split())
        print("%d %d" % (n, m), end=" ")
        if n > m:
            n, m = m, n
        s = []
        for i in range(n, m + 1):
            temp = []
            if i == 1:
                pass
            else:
                temp.append(i)
                sub = i
                while True:
                    if sub == 1:
                        break
                    else:
                        if sub % 2 != 0:
                            sub = sub * 3 + 1
                        else:
                            sub = sub // 2
                        temp.append(sub)
                s.append(len(temp))
        print(max(s))
        s.clear()
    except EOFError:
        break

# 使用字典，儲存找過的值
# 這個版本才會過
appeared = {}  # 記錄計算過的數字


def solve(i, j):
    ans = 0
    for cur in range(min(i, j), max(i, j) + 1):  # 注意i, j大小
        count = 0
        n = cur
        while True:
            if n in appeared:  # 如果n之前有計算過，就直接取之前紀錄的值加上去，然後跳出迴圈
                count += appeared[n]
                break

            count += 1
            if n == 1:
                break
            if n % 2 != 0:
                n = 3 * n + 1
            else:
                n = n // 2

        appeared[cur] = count  # 記錄目前數字會進入迴圈幾次
        ans = max(count, ans)

    return f'{i} {j} {ans}'


while True:
    try:
        i, j = list(map(int, input().split()))
        print(solve(i, j))
    except EOFError:
        break
