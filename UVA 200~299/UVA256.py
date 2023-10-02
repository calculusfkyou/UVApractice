def main():
    quirk_numbers = []

    # The largest possible quirk number is 99999999.
    for n in range(10000):
        quirk_numbers.append(n * n)

    while True:
        try:
            d = int(input())
            for num in quirk_numbers:
                # Consider all numbers up to d digits.
                if num >= 10 ** d:
                    break

                U = num // 10 ** (d // 2)
                L = num % 10 ** (d // 2)
                if (U + L) ** 2 == num:
                    print(f"{num:0{d}}")
        except EOFError:
            break


if __name__=="__main__":
    main()