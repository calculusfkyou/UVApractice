# 就是一個公式，可以記
import math

s, distance = 0, 0
while True:
    try:
        r, degree, unit = input().split()
        r = int(r)
        degree = int(degree)
        if unit == "min":
            degree = degree / 60
        s = 2 * math.pi * (r + 6440) * (degree / 360)
        distance = 2 * (r + 6440) * math.sin(degree * math.pi / 180 / 2)
        print("%.6f %.6f" % (round(s, 6), round(distance, 6)))
        s, distance = 0, 0
    except EOFError:
        break
