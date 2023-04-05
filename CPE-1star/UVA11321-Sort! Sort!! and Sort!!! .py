while True:
	try:
		n,m=map(int,input().split())
		if n==0 and m==0:
			break
		nums=[]
		for i in range(n):
			num=int(input())
			if num>0:
				nums.append([num,num%m])
			else:
				nums.append([num,-(abs(num)%m)])
		o,O=map(int,input().split())
		temp=[]
		for i in range(len(nums)):
			if nums[i][0]%2!=0:
				temp.append(nums[i])
		temp.sort(key=lambda temp:temp[0],reverse=1)
		temp2=[]
		for i in range(len(nums)):
			if nums[i][0]%2==0:
				temp2.append(nums[i])
		temp2.sort(key=lambda temp:temp[0])
		nums=temp[:]+temp2[:]
		nums.sort(key=lambda nums:(nums[1]))
		print(n,end=" ")
		print(m)
		for i in range(len(nums)):
			print(nums[i][0])
		print(0,end=" ")
		print(0)
	except:
		break