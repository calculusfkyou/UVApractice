def main():
    while True:
        try:
            x = int(input())
            y = int(input())
            print(x * y)
        except EOFError:
            break


if __name__ == "__main__":
    main()
