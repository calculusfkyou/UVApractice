# 計算幾進位，n的每個位數加起來要整除(進位-1)，注意1和0
# A~Z=10~35
# a~z=36~61
# v1
while True:
    try:
        n = input()
        if n[0] == "+" or n[0] == "-":
            n = n[1:]
        c = 61  # 最大位數
        if len(n) < 2:
            if n[-1].isalpha():
                if n[-1] >= 'A' and n[0] <= 'Z':
                    c = ord(n[-1]) - 55
                elif n[-1] >= 'a' and n[0] <= 'z':
                    c = ord(n[-1]) - 61
            else:
                c = int(n[-1])
        count = 0
        while len(n) > 0:
            temp = n[-1]
            if temp.isalpha():
                if temp >= 'A' and temp <= 'Z':
                    temp = ord(n[-1]) - 55
                elif temp >= 'a' and temp <= 'z':
                    temp = ord(n[-1]) - 61
            else:
                temp = int(n[-1])
            if temp > c:
                c = temp
            count += temp
            n = n[:-1]
        check = 0
        if count == 1 or count == 0:
            print(2)
        else:
            while c > 1:
                if count % c == 0:
                    check = 1
                    break
                c -= 1
            if check:
                print(c + 1)
            else:
                print("such number is impossible!")
    except EOFError:
        break

# v2
# 建議參考
while 1:
    try:
        n = input()
        d, maximum, total, ans = 0, 1, 0, 0
        for i in range(len(n)):
            if n[i] >= '0' and n[i] <= "9":
                d = ord(n[i]) - ord("0")
            if n[i] >= "A" and n[i] <= "Z":
                d = ord(n[i]) - ord("A") + 10
            if n[i] >= "a" and n[i] <= "z":
                d = ord(n[i]) - ord("a") + 36
            total += d
            if d > maximum:
                maximum = d
        for i in range(maximum + 1, 63):
            if total % (i - 1) == 0:
                ans = i
                break
        if ans <= 62 and ans != 0:
            print(ans)
        else:
            print("such number is impossible!")
    except:
        break
