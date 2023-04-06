while True:
	try:
		N=int(input())
		if N==0:
			break
		if N%9!=0:
			print("%d is not a multiple of 9."%(N))
		else:
			temp=0
			subN=N
			degree=1
			while subN%9==0:
				while subN>0:
					temp+=subN%10
					subN=subN//10
				if temp%9==0:
					degree+=1
				subN=temp
			print("%d is a multiple of 9 and has 9-degree %d."%(N,degree))
	except:
		break