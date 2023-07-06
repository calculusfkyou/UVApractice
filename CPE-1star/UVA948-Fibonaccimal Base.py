list=[1,1]
for i in range(2,2000):
	list.append(list[i-1]+list[i-2])
list.pop(0)
list.reverse()
while True:
	try:
		n=int(input())
		for i in range(n):
			num=int(input())
			temp=[]
			numm=num
			for k in range(len(list)):
				if list[k]<=numm and list[k-1]>numm:
					temp.append(1)
					numm=numm-list[k]
				else:
					temp.append(0)
			while temp[0]==0:
				temp.pop(0)
			temp.reverse()
			bs,ans=0,0
			for j in temp:
				ans+=j*(10**bs)
				bs+=1
			print("%d = %d (fib)"%(num,ans))
			temp.clear()
			
	except EOFError:
		break