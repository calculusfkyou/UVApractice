def main():
    n = int(input())
    for i in range(n):
        m = int(input())
        b1 = bin(m)[2:].count("1")
        temp, bs = 0, 0
        while m > 0:
            temp += (m % 10) * (16 ** bs)
            bs += 1
            m = m // 10
        b2 = bin(temp).count("1")
        print(b1, b2)


if __name__ == "__main__":
    main()
