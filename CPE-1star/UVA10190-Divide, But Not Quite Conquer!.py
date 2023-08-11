data=[]
while True:
	a,b=map(int,input().split())
	if a!=1 and b!=1:
		data.append(a)
		while a>1 and a%b==0:
			a=a//b
			data.append(a)
		if data[-1]!=1:
			print("Boring!",end="")
		if data[-1]==1:
			for i in data:
				if i!=1:
					print(i,end=" ")
				if i==1:
					print(i,end="")
	else:
		print("Boring!",end="")
	print()
	data=[] 
       
# V2
while True:
	try:
		n,m=map(int,input().split())
		ans=[n]
		if m==1 or m==0:
			print("Boring!")
		else:
			while n-int(n)==0 and n!=1:
				n=n/m
				if n-int(n)==0:
					ans.append(int(n))
			if ans[-1]==1:
				print(*ans)
			else:
				print("Boring!")
	except EOFError:
		break     