#只有兩個國家，直接算就好
# while True:
# 	try:
# 		n=int(input())
# 		England,Spain=0,0
# 		for i in range(n):
# 			country,woman,last=input().split()
# 			if country=="England":
# 				England+=1
# 			else:
# 				Spain+=1
# 		print("England %d"%(England))
# 		print("Spain %d"%(Spain))	
			
# 	except:
# 		break

while True:
	try:
		n=int(input())
		name=[]
		for i in range(n):
			line=input().split()
			l=line[0]
			if i>0:
				check=1
				for j in range(len(name)):
					if name[j][0]==l:
						name[j][1]+=1
						check=0
						break
				if check:
					name.append([l,1])
			else:
				name.append([l,1])
		name.sort(key=lambda name:name[0])
		for i in range(len(name)):
			print(*name[i])
	except:
		break