# 建議觀看此影片: https://www.youtube.com/watch?v=lSh7iT8cnYk&t=221s

while 1:
    try:
        n = int(input())
        nums = []
        for i in range(n):
            nums.append(int(input()))
        nums.sort()
        minimum, maximum = 0, 0
        if n % 2 == 1:
            minimum = nums[n // 2]
            maximum = nums[n // 2]
        else:
            minimum = nums[n // 2 - 1]
            maximum = nums[n // 2]
        count = 0
        for i in range(n):
            if minimum <= nums[i] <= maximum:
                count += 1
        possible = maximum - minimum + 1
        print(minimum, count, possible)
    except EOFError:
        break
