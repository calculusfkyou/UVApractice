def main():
    while True:
        try:
            v, t = map(int, input().split())
            print(v * t * 2)
        except EOFError:
            break


if __name__ == "__main__":
    main()
