# def main(s, d):
#     while d > 0:
#         d = d - s
#         s += 1
#     return (s - 1)
#
#
# if __name__ == "__main__":
#     while True:
#         try:
#             s, d = map(int, input().split())
#             print(main(s, d))
#         except EOFError:
#             break

from sys import stdin
import math

for f in stdin:

    S, D = map(int, f.split())

    f = (2 * D) + (S * S) - S

    ans = ((-1 + ((1 - (4 * (-f))) ** 0.5)) / 2)

    print(math.ceil(ans))
