def main():
    while True:
        try:
            s = int(input())
            for i in range(s):
                n, p, i = map(float, input().split())
                q = 1 - p
                if p == 0:
                    winrate = 0.0
                else:
                    winrate = pow(q, (i - 1)) * p / (1 - pow(q, n))
                print("%.4f" % (winrate))
        except EOFError:
            break


if __name__ == "__main__":
    main()
