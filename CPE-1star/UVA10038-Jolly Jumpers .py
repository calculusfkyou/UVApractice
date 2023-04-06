#每兩個相差在1~n-1
#相差不能一樣
while True:
	try:
		n=list(map(int,input().split()))
		temp=[]
		check=0
		count=0
		for i in range(1,len(n)-1):
			temp.append(abs(n[i]-n[i+1]))
		for i in range(len(temp)):
			if temp[i]>(n[0]-1) or temp[i]<1:
				count+=1
			check=temp.count(temp[i])
			if check>1:
				count+=1
		if count!=0:
			print("Not jolly")
		else:
			print("Jolly")
	except EOFError:
		break