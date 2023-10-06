def main():
    while True:
        try:
            n = int(input())
            if n < 0:
                break
            print(1 + (n + 1) * n // 2)
        except:
            break


if __name__ == "__main__":
    main()
