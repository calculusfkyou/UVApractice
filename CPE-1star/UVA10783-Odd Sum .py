while True:
	try:
		n=int(input())
		count=1
		for i in range(n):
			a=int(input())
			b=int(input())
			temp=0
			for j in range(a,b+1):
				if j%2!=0:
					temp+=j
			print("Case %d: %d"%(count,temp))
			count+=1
	except:
		break