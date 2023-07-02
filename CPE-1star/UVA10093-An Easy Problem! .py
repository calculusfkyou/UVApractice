#計算幾進位，n的每個位數加起來要整除(進位-1)，注意1和0
#A~Z=10~35
#a~z=36~61
while True:
	try:
		n=input()
		if n[0]=="+" or n[0]=="-":
			n=n[1:]
		c=61#最大位數
		if len(n)<2:
			if n[-1].isalpha():
				if n[-1]>='A' and n[0]<='Z':
					c=ord(n[-1])-55
				elif n[-1]>='a' and n[0]<='z':
					c=ord(n[-1])-61
			else:
				c=int(n[-1])
		count=0
		while len(n)>0:
			temp=n[-1]
			if temp.isalpha():
				if temp>='A' and temp<='Z':
					temp=ord(n[-1])-55
				elif temp>='a' and temp<='z':
					temp=ord(n[-1])-61
			else:
				temp=int(n[-1])
			if temp>c:
				c=temp
			count+=temp
			n=n[:-1]
		check=0
		if count==1 or count==0:
			print(2)
		else:
			while c>1:
				if count%c==0:
					check=1
					break
				c-=1		
			if check:
				print(c+1)
			else:
				print("such number is impossible!")	
	except EOFError:
		break