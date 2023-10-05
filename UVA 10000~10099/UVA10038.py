def main():
    while True:
        try:
            nums = list(map(int, input().split()))
            jolly = [i for i in range(1, nums[0])]
            nums = nums[1:]
            check = 1
            for i in range(len(nums) - 1):
                diff = abs(nums[i] - nums[i + 1])
                if diff not in jolly:
                    check = 0
                    break
                else:
                    jolly.remove(diff)
            if check:
                print("Jolly")
            else:
                print("Not jolly")
        except EOFError:
            break


if __name__ == "__main__":
    main()
