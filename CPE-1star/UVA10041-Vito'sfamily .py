#求中位數，再求中位數距離每個鄰居的和
import statistics
while True:
	try:
		n=int(input())
		for i in range(n):
			nums=list(map(int,input().split()))
			nums.pop(0)
			mid=statistics.median(nums)
			distance=0
			for j in range(len(nums)):
				distance+=abs(mid-nums[j])
			print(int(distance))
	except EOFError:
		break