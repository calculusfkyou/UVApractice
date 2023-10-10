def main():
    skylines = [0] * 10005
    Rightest = 0
    while True:
        try:
            L, H, R = map(int, input().split())
            if R > Rightest:
                Rightest = R
            for i in range(L, R):
                if H > skylines[i]:
                    skylines[i] = H
        except EOFError:
            break
    # for i in range(8):
    #     L, H, R = map(int, input().split())
    #     if R > Rightest:
    #         Rightest = R
    #     for i in range(L, R):
    #         if H > skylines[i]:
    #             skylines[i] = H
    # print(skylines)
    # print(Rightest)
    now = 0
    for i in range(Rightest):
        if skylines[i] != now:
            print(i, skylines[i], end=" ")
            now = skylines[i]
    print(Rightest,0)


if __name__ == "__main__":
    main()