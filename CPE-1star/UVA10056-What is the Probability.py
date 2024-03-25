# 請看此影片: https://www.youtube.com/watch?v=soxR1USFDK0
while True:
    try:
        s = int(input())
        for i in range(s):
            n, p, k = map(float, input().split())
            q = 1 - p
            if p == 0:
                winrate = 0.0
            else:
                winrate = pow(q, (k - 1)) * p / (1 - pow(q, n))
            print("%.4f" % winrate)
    except EOFError:
        break
