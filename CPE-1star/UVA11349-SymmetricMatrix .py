Test=1
while True:
	try:
		t=int(input())
		for j in range(t):
			neg=0
			case=input().split()
			n=int(case[2])
			matrix=[]
			for i in range(n):
				inp=list(map(int,input().split()))
				matrix.append(inp)
				for k in inp:
					if k<0:
						neg+=1
			if n==1 and neg==0:
				print("Test #%d: Symmetric."%(Test))
				Test+=1
			elif neg==0:
				check=0
				temp=[]
				mid=n//2
				for i in range(mid):
					temp=matrix[n-1-i]
					temp.reverse()
					if temp==matrix[i]:
						check+=1
				temp=matrix[mid]
				temp.reverse()
				if temp==matrix[mid]:
					check+=1
				if check==mid+1:
					print("Test #%d: Symmetric."%(Test))
					Test+=1
				else:
					print("Test #%d: Non-symmetric."%(Test))
					Test+=1
			else:
				print("Test #%d: Non-symmetric."%(Test))
				Test+=1
	except EOFError:
		break