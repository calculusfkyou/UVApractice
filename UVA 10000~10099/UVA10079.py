# 數學題
# 1刀2塊->1+1=2
# 2刀4塊->1+1+2=4
# 3刀7塊->1+(1+2+3)=7
# 4刀11塊->1+(1+2+3+4)=11
# 5刀16塊->1+(1+2+3+4+5)=16
def main():
    while True:
        try:
            n = int(input())
            if n < 0:
                break
            print(1 + (n + 1) * n // 2)
        except:
            break


if __name__ == "__main__":
    main()
