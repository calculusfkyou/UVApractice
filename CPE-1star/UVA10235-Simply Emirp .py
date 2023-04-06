#先判斷是否為質數，不是則不為prime，再判斷reverse過是否為質數，是則為emirp，不是則為prime
while True:
	try:
		N=int(input())
		count=0
		for i in range(1,N+1):
			if N%i==0:
				count+=1
		
		subN=N
		temp=[]
		while subN>0:
			temp.append(subN%10)
			subN=subN//10
		temp2=temp[:]
		temp2.reverse()
		reverseN=0
		for i in range(len(temp2)):
			reverseN+=temp2[i]*(10**i)
		count2=0
		if reverseN!=N:
			for i in range(1,reverseN+1):
				if reverseN%i==0:
					count2+=1
		
		if count==2 and count2==2:
			print("%d is emirp."%(N))
		elif count==2 and count2!=2:
			print("%d is prime."%(N))
		else:
			print("%d is not prime."%(N))
	except EOFError:
		break