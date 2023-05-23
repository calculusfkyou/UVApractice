# 輸入一數，將其轉換成二進位和十六進位並計算各有多少個1
while True:
	try:
		n=int(input())
		for i in range(n):
			m=int(input())
			subm=m
			bs=0
			hm=0
			count=0
			while subm>0:
				if subm%2==1:
					count+=1
				subm=subm//2
			print(count,end=" ")
			count=0
			while m>0:
				temp=m%10
				while temp>0:
					if temp%2==1:
						count+=1
					temp=temp//2
				m=m//10
			print(count)
	except EOFError:
		break