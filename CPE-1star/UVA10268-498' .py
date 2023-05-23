#按照他給的第二個式子求導數即可
while True:
	try:
		x=int(input())
		nums=list(map(int,input().split()))
		n=len(nums)-1
		subn=n-1
		ans=0
		for i in range(len(nums)):
			ans+=n*(nums[i]*(x**subn))
			n-=1
			subn-=1
		print(int(ans))
	except EOFError:
		break

#2
while True:
	try:
		x=int(input())
		n=list(map(int,input().split()))
		nn=len(n)-1
		nnn=len(n)-2
		ans=0
		for i in range(len(n)-1):
			ans+=nn*n[i]*(x**nnn)
			nn-=1
			nnn-=1
		print(int(ans))
	except:
		break