#任意兩項的和都要不一樣
no=1	
while True:
	try:
		n=input()
		if n==" ":
			pass
		else:
			nums=list(map(int,input().split()))
			temp=[]
			for i in range(len(nums)):
				for j in range(i+1,len(nums)):
					temp.append(nums[i]+nums[j])
			check=0
			for i in range(len(temp)):
				count=temp.count(temp[i])
				if count>1:
					check+=1
			if check!=0:
				print("Case #%d: It is not a B2-Sequence."%(no))
			else:
				print("Case #%d: It is a B2-Sequence."%(no))
			print()
			no+=1
	except EOFError:
		break