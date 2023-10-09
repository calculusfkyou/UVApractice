# 使用這個函式的寫法超時
# import statistics
#
#
# def main():
#     nums = []
#     while True:
#         try:
#             nums.append(int(input()))
#             print(int(statistics.median(nums)))
#         except:
#             break
#
#
# if __name__ == "__main__":
#     main()

N = []
while True:
    try:
        num = int(input())
        N.append(num)
        N.sort()
        middle = len(N) // 2
        if len(N) % 2 == 1:
            print(N[middle])
        else:
            median = (N[middle] + N[middle - 1]) // 2
            print(median)
    except EOFError:
        break
