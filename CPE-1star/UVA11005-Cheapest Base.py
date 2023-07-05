#找到最小進為花費，若有相同的，則也印出，建議收看: https://www.youtube.com/watch?v=z8cM3pTXqUI
case=1
n=int(input())
for c in range(n):
	try:
		print("Case %d:"%(case))
		cost=[]
		for i in range(4):
			num=list(map(int,input().split()))
			cost.extend(num) 
		line=int(input())
		for i in range(line):
			x=int(input())
			cost2=[]
			for base in range(2,37):
				total=0
				temp=x
				while temp>0:
					re=temp%base
					total=total+cost[re]
					temp=temp//base
				cost2.append([base,total])
			cost2.sort(key=lambda cost2:cost2[1])
			print("Cheapest base(s) for number %d:"%(x),end="")
			minimum=cost2[0][1]
			for base in range(len(cost2)):
				if cost2[base][1]==minimum:
					print(" %d"%(cost2[base][0]),end="")
				else:
					break
			print()
		if case<n:
			print()
		case+=1
	except EOFError:
		break