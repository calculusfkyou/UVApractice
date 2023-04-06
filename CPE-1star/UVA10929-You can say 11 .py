#是否為11的倍數
while True:
	try:
		n=int(input())
		if n==0:
			break
		if n%11==0:
			print("%d is a multiple of 11."%(n))
		else:
			print("%d is not a multiple of 11."%(n))
	except:
		break
