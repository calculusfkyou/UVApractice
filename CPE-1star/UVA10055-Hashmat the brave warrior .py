#差的絕對值
while True:
	try:
		n,m=map(int,input().split())
		print(abs(m-n))
	except EOFError:
		break