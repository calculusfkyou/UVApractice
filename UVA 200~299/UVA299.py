def bubblesort(train):
    count = 0
    for i in range(len(train) - 1):
        for j in range(len(train) - 1):
            if train[j] > train[j + 1]:
                train[j + 1], train[j] = train[j], train[j + 1]
                count += 1
    return count


def main():
    n = int(input())
    for i in range(n):
        l = int(input())
        train = list(map(int, input().split()))
        count = bubblesort(train)
        print("Optimal train swapping takes %d swaps." % count)


if __name__ == "__main__":
    main()
