#將兩字串轉十進位，找公因數，若等於1則fail 
import math
while True:
	try:
		N=int(input())
		no=1
		for i in range(N):
			s1=int(input())
			s2=int(input())
			bs=0
			bs1,bs2=0,0
			while s1>0:
				bs1+=(s1%10)*(2**bs)
				s1=s1//10
				bs+=1
			bs=0
			while s2>0:
				bs2+=(s2%10)*(2**bs)
				s2=s2//10
				bs+=1
			m=math.gcd(bs1,bs2)
			if m!=1:
				print("Pair #%d: All you need is love!"%(no))
			else:
				print("Pair #%d: Love is not all you need!"%(no))
			no+=1
	except EOFError:
		break