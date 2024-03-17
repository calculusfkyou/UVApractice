# 解法見：https://www.youtube.com/watch?v=vtLq9C0NWF0&list=PLYhy6KLAgQE6QpZ5dUz-p-5dC1bWCTuIi&index=39
# GPT寫的
while True:
    try:
        nums = list(map(float, input().split()))
        x1, y1, x2, y2, x3, y3, x4, y4 = nums
        if x1 == x3 and y1 == y3:
            print("%.3f %.3f" % (x2 + x4 - x3, y2 + y4 - y3))
        elif x1 == x4 and y1 == y4:
            print("%.3f %.3f" % (x2 + x3 - x4, y2 + y3 - y4))
        elif x2 == x3 and y2 == y3:
            print("%.3f %.3f" % (x1 + x4 - x3, y1 + y4 - y3))
        else:
            print("%.3f %.3f" % (x1 + x3 - x4, y1 + y3 - y4))
    except EOFError:
        break

# 正確寫法
while True:
    try:
        x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())
        x = x1 + x2 + x3 + x4
        y = y1 + y2 + y3 + y4
        if (x1 == x3 and y1 == y3) or (x1 == x4 and y1 == y4):
            print("%.3f %.3f" % (x - x1 * 3, y - 3 * y1))
        else:
            print("%.3f %.3f" % (x - x2 * 3, y - y2 * 3))
    except:
        break
