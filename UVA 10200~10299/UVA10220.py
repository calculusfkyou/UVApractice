# 算出n的階層的每一位總和
import math


def main():
    while True:
        try:
            n = int(input())
            temp = math.factorial(n)
            sum = 0
            while temp > 0:
                sum += temp % 10
                temp = temp // 10
            print(sum)
        except EOFError:
            break


if __name__ == "__main__":
    main()
