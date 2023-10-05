def reverse_check(p):
    if len(p) % 2 == 1:
        if p[:len(p) // 2] == p[len(p) // 2 + 1:][::-1]:
            return True
    else:
        if p[:len(p) // 2] == p[len(p) // 2:][::-1]:
            return True
    return False


def main():
    n = int(input())
    for i in range(n):
        p = input()
        count = 0
        while not reverse_check(p):
            p = str(int(p) + int(p[::-1]))
            count += 1
        print(count, p)


if __name__ == "__main__":
    main()
