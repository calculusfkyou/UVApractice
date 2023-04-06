#相乘再乘2
while True:
	try:
		n,m=map(int,input().split())
		print(n*m*2)
	except EOFError:
		break