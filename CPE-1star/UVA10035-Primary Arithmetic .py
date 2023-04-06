#計算進位次數
while True:
	try:
		n,m=map(int,input().split())
		if n==0 and m==0:
			break
		carry=0
		while True:
			try:
				if n==0 and m==0:
					break
				if n%10+m%10>=10:
					carry+=1
					n=n/10+1
					m/=10
				else:
					n/=10
					m/=10
			except:
				break
		if carry==0:
			print("No carry operation.")
		elif carry==1:
			print("1 carry operation.")
		else:
			print("%d carry operations."%(carry))
	except:
		break
		
