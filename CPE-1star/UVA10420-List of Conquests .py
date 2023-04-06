#只有兩個國家，直接算就好
while True:
	try:
		n=int(input())
		England,Spain=0,0
		for i in range(n):
			country,woman,last=input().split()
			if country=="England":
				England+=1
			else:
				Spain+=1
		print("England %d"%(England))
		print("Spain %d"%(Spain))	
			
	except:
		break