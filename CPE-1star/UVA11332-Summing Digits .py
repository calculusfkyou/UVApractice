while True:
	try:
		n=int(input())
		if n==0:
			break 
		while n>=10:
			temp=0
			while n>0:
				temp+=n%10
				n=n//10
			n=temp
			temp=0
		print(n)
	except EOFError:
		break