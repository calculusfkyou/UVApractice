fib = [1, 1]
for i in range(2000):
    fib.insert(0, fib[0] + fib[1])
fib.pop()


def main():
    for i in range(int(input())):
        pos_int = int(input())
        temp = pos_int
        ans = ""
        for j in range(len(fib)):
            if pos_int >= fib[j]:
                ans += "1"
                pos_int -= fib[j]
            else:
                ans += "0"
        ans = ans.lstrip("0")
        print("%d = %s (fib)" % (temp, ans))


if __name__ == "__main__":
    main()
