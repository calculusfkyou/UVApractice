def main():
    while True:
        try:
            a, b = map(int, input().split())
            if a + b == 0:
                break
            carry, carrydigit = 0, 0
            digitsum = 0
            while a > 0 or b > 0:
                digitsum = a % 10 + b % 10 + carrydigit
                if digitsum < 10:
                    carrydigit = 0
                else:
                    carry += 1
                    carrydigit = 1
                a=a//10
                b=b//10
            if carry == 0:
                print("No carry operation.")
            elif carry == 1:
                print("1 carry operation.")
            else:
                print(carry, "carry operations.")
        except:
            break


if __name__ == "__main__":
    main()
