def main(n):
    referenceX, referenceY = map(int, input().split())
    for i in range(n):
        x, y = map(int, input().split())
        if x == referenceX or y == referenceY:
            print("divisa")
            continue
        if x > referenceX and y > referenceY:
            print("NE")
        elif x < referenceX and y > referenceY:
            print("NO")
        elif x < referenceX and y < referenceY:
            print("SO")
        else:
            print("SE")
    return


if __name__ == "__main__":
    while 1:
        n = int(input())
        if n == 0:
            break
        main(n)
