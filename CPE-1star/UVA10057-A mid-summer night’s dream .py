#建議觀看此影片: https://www.youtube.com/watch?v=lSh7iT8cnYk&t=221s
"""
對於每組測資，輸出三個整數。
第一個數字是能得到該算式最小值的A。
第二個數字是|Xi − A|為最小值的數量。
第三行數字是可能有幾種最小值。
"""
while True:
	try:
		n=int(input())
		nums=[]
		for i in range(n):
			num=int(input())
			nums.append(num)
		nums.sort()
		mid,mid1,mid2=0,0,0
		A,Asum,allsum=0,0,0
		if n%2==0:#偶數個整數
			mid1=nums[n//2-1]
			mid2=nums[n//2]
			temp=[]
			for i in range(mid1,mid2+1):
				count=0
				for j in range(len(nums)):
					count+=abs(i-nums[j])
				temp.append([count,i])
			temp.sort(key=lambda temp:temp[0])
			count=temp[0][0]
			for i in range(len(temp)):
				if temp[i][0]==count:
					allsum+=1
					if temp[i][1]==mid1:
						Asum+=1
						A=mid1
					elif temp[i][1]==mid2:
						Asum+=1
						if Asum==1:
							A=mid2
			if Asum==2:
				c=nums.count(mid1)
				cc=nums.count(mid2)
				Asum=c+cc
			else:
				c=nums.count(A)
				Asum=c
		else:#奇數個
			mid=nums[n//2]
			allsum=1
			A=mid
			Asum=nums.count(A)			
		print("%d %d %d"%(A,Asum,allsum))
	except EOFError:
		break