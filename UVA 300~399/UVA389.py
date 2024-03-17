while 1:
    try:
        num, base, convertbase = input().split()
        base, convertbase = int(base), int(convertbase)
        num = int(num, base)  # 轉10進位
        if convertbase == 0:
            print("  ERROR")
        else:
            ans = ""
            if convertbase == 10:
                ans = str(num)
            else:
                while num > 0:
                    remainder = num % convertbase
                    if remainder >= 10:
                        ans += chr(ord('A') + remainder - 10)
                    else:
                        ans += str(remainder)
                    num = num // convertbase
                ans = ans[::-1]
            if len(ans) <= 7:
                print("%7s" % ans)
            else:
                print("  ERROR")
    except EOFError:
        break
