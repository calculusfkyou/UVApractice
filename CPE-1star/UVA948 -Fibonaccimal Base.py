#用1 0 轉換成費式數列的樣子
#1
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

#2
listP=[]
listP.append(0)
listP.append(1)
for i in range(2,1000):
	listP.append(listP[i-1]+listP[i-2])	
N=int(input())
for i in range(N):
	ans=0
	num=int(input())
	NUM=num
	for j in range(len(listP)):
		if listP[j]<=num and listP[j+1]>=num:
			for k in range(j+2,0,-1):
				if listP[k]<=num and listP[k+1]>=num:
					num-=listP[k]
					ans+=10**(k-2)
				if num==0:
					break
	print("%d = %d (fib)"%(NUM,ans))