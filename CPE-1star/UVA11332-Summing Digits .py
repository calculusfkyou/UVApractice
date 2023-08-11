#計算每個位數相加，直到小於10
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

# V2
def stoi(num):
    for i in range(len(num)):
        num[i]=int(num[i])
    return num
while True:
    try:
        n=list(input())
        if n==["0"]:
        	break
        ans=n[0]
        while len(n)>1:
            n=stoi(n)
            ans=sum(n)
            n=list(str(ans))
        print(ans)
    except:
        break