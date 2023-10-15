from statistics import median


def main():
    while 1:
        try:
            n = int(input())
            coins = [int(input()) for i in range(n)]
            avg = sum(coins) // n
            c = [0]
            for i in range(1, n):
                c.append(c[i - 1] + coins[i] - avg)
            c.sort()
            mid = median(c)
            ans = 0
            for i in range(n):
                ans += abs(mid - c[i])
            print(int(ans))
        except EOFError:
            break


if __name__ == "__main__":
    main()
