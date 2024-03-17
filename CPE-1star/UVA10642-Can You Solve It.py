# 對角線關係，建議收看:https://www.youtube.com/watch?v=mgoIwBhOx2A&list=PLYhy6KLAgQE6QpZ5dUz-p-5dC1bWCTuIi&index=38
def location(x, y):
    return (x + y) * (x + y + 1) // 2 + x


case = 1
while True:
    try:
        n = int(input())
        for i in range(n):
            x1, y1, x2, y2 = map(int, input().split())
            print("Case %d: %d" % (case, location(x2, y2) - location(x1, y1)))
            case += 1
    except EOFError:
        break
