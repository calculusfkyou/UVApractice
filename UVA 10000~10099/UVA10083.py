# WA 要解決精度問題
def main():
    while True:
        try:
            t, a, b = map(int, input().split())
            division = (t ** a - 1) / (t ** b - 1)
            if division != int(division):
                print("(%d^%d-1)/(%d^%d-1) is not an integer with less than 100 digits." % (t, a, t, b))
            else:
                print("(%d^%d-1)/(%d^%d-1) %d" % (t, a, t, b, int(division)))
        except:
            if OverflowError:
                print("(%d^%d-1)/(%d^%d-1) is not an integer with less than 100 digits." % (t, a, t, b))
            if EOFError:
                break


if __name__ == "__main__":
    main()
