#氣泡排序，由小到大，計算交換的次數
def bbsort(subnum):
	count=0
	for k in range(len(subnum)-1):
		for j in range(0,len(subnum)-1):
			if subnum[j]>subnum[j+1]:
				temp=subnum[j+1]
				subnum[j+1]=subnum[j]
				subnum[j]=temp
				count+=1
	return count
	
while True:
	try:
		n=int(input())
		for i in range(n):
			l=int(input())
			nums=list(map(int,input().split()))
			print("Optimal train swapping takes %d swaps."%(bbsort(nums)))
	except EOFError:
		break
