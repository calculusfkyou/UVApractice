while True:
	try:
		temp,temp2=[],[]
		n,m=map(int,input().split())
		subn,subm=n,m
		if n>m:
			tempp=n
			n=m
			m=tempp
		for i in range(n,m+1):
			if i==1:
				pass
			else:
				temp.append(i)
				while True:
					if i==1:
						break
					else:
						if i%2!=0:
							i=i*3+1
							temp.append(i)
						else:
							i=i//2
							temp.append(i)
				temp2.append(len(temp))
				temp.clear()
		print("%d %d %d"%(subn,subm,max(temp2)))
		temp2.clear()
	except EOFError:
		break
