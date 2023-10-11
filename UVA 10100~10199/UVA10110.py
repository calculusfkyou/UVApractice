from math import sqrt


def main():
    while True:
        try:
            n = int(input())
            if n == 0:
                break
            if int(sqrt(n) != int(sqrt(n))):
                print("no")
            else:
                print("yes")
        except:
            break


if __name__ == "__main__":
    main()
