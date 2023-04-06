#計算輸入轉換成二進位後有多少個1
while True:
	try:
		n=int(input())
		if n==0:
			break
		bs=0
		temp=0
		count=0
		while n>0:
			temp=temp+(n%2)*(10**bs)
			if n%2==1:
				count+=1
			n=n//2
			bs+=1
		print("The parity of %d is %d (mod 2)."%(temp,count))
	except:
		break