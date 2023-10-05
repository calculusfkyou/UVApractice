def main():
    t = int(input())
    for i in range(t):
        n = int(input())  # 天數
        p = int(input())  # 政黨數
        record = []
        for j in range(p):
            h = int(input())
            for k in range(h, n+1, h):
                if k not in record:
                    if k % 7 != 6 and k % 7 != 0:
                        record.append(k)
        # print(record)
        print(len(record))


if __name__ == "__main__":
    main()
