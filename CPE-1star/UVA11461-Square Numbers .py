#判斷範圍內的完全平方數有幾個
import math
while True:
	try:
		a,b=map(int,input().split())
		if a==0 and b==0:
			break
		count=0
		for i in range(a,b+1):
			temp=math.sqrt(i)
			if temp-int(temp)==0:
				count+=1
		print(count)
	except:
		break