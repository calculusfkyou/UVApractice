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
			degree=0
			while subN%9==0:
				while subN>0:
					temp+=subN%10
					subN=subN//10
				if temp%9==0:
					degree+=1
				subN=temp
				temp=0
				if subN==9:#注意變成9的時候
					break
			print("%d is a multiple of 9 and has 9-degree %d."%(N,degree))
	except:
		break