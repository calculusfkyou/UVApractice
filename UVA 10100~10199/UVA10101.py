def main():
    sequence = 1
    while True:
        try:
            n = int(input())
            temp = []
            if n == 0:
                temp.append(0)
            else:
                while n > 0:
                    temp2 = n % 100
                    if temp2 != 0:
                        temp.append(temp2)
                    n = n // 100
                    if n == 0:
                        break

                    temp2 = n % 10
                    if temp2 != 0:
                        temp.append("shata")
                        temp.append(temp2)
                    n = n // 10
                    if n == 0:
                        break

                    temp2 = n % 100
                    if temp2 != 0:
                        temp.append("hajar")
                        temp.append(temp2)
                    n = n // 100
                    if n == 0:
                        break

                    temp2 = n % 100
                    if temp2 != 0:
                        temp.append("lakh")
                        temp.append(temp2)
                    n = n // 100
                    if n == 0:
                        break

                    if n != 0:
                        temp.append("kuti")
            temp.reverse()
            if sequence < 10:
                print("   %d. " % sequence, end="")
            else:
                print("   %d. " % sequence, end="")
            sequence += 1

            for i in range(len(temp) - 1):
                print(temp[i], end=" ")
            print(temp[-1])
        except EOFError:
            break


if __name__ == "__main__":
    main()
