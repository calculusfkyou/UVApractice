def main():
    while True:
        try:
            n=float(input())
            p=float(input())
            result = int(p ** (1.0 / n) + 0.5)
            print(result)
        except EOFError:
            break


if __name__ == "__main__":
    main()
