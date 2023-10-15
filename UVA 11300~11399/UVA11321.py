# 小心負數的餘數，不是直接mod，而是要取正後mod再加負號
def negMod(num, m):
    if num < 0:
        return -(abs(num) % m)
    else:
        return num % m


def main():
    while 1:
        try:
            n, m = map(int, input().split())
            print(n, m)
            if n + m == 0:
                break
            odd, even = [], []
            for i in range(n):
                temp = int(input())
                if temp % 2 == 0:
                    even.append([temp, negMod(temp, m)])
                else:
                    odd.append([temp, negMod(temp, m)])
            # 以除以m的餘數由小到大排
            even.sort(key=lambda even: even[0])  # 偶數的餘數相等，較小的偶數在前面
            even.sort(key=lambda even: even[1])  # 先排偶數再排餘數
            odd.sort(key=lambda odd: odd[0], reverse=1)  # 奇數的餘數相等，較大的奇數在前面
            odd.sort(key=lambda odd: odd[1])
            ans = odd + even  # 奇數在偶數前面
            ans.sort(key=lambda even: even[1])  # 按照餘數大小排序
            for i in range(len(ans)):
                print(ans[i][0])
        except:
            break


if __name__ == "__main__":
    main()
