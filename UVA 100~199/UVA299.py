def bubble_sort(carriages):
    count = 0
    for i in range(len(carriages) - 1):
        for j in range(len(carriages) - 1):
            if carriages[j] > carriages[j + 1]:
                carriages[j], carriages[j + 1] = carriages[j + 1], carriages[j]
                count += 1
    return count


def main():
    n = int(input())
    for i in range(n):
        l = int(input())
        carriages = list(map(int, input().split()))
        print("Optimal train swapping takes %d swaps." % bubble_sort(carriages))


if __name__ == "__main__":
    main()
