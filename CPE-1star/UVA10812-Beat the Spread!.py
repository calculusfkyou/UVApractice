#兩數加起來除2和兩數相減除2
while True:
	try:
		n=int(input())
		for i in range(n):
			s,d=map(int,input().split())
			if s<d or (s-d)%2!=0:
				print("impossible")
			else:
				print(d+(s-d)//2,end=" ")
				print((s-d)//2)				
	except:
		break

#2
while True:
	try:
		n=int(input())
		for i in range(n):
			s,d=map(int,input().split())
			if s<d or (s-d)%2!=0:
				print("impossible")
			else:
				print((s+d)//2,end=" ")
				print((s-d)//2)
	except:
		break