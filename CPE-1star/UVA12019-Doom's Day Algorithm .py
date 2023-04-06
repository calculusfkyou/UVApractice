#計算那天是星期幾，我暴力解
while True:
	try:
		case=int(input())
		for i in range(1,case+1):
			M,D=map(int,input().split())
			if M==2 or M==3:
				if D%7==4:
					print("Friday")
				elif D%7==5:
					print("Saturday")
				elif D%7==6:
					print("Sunday")
				elif D%7==0:
					print("Monday")
				elif D%7==1:
					print("Tuesday")
				elif D%7==2:
					print("Wednesday")
				elif D%7==3:
					print("Thursday")
			elif M==12 or M==9:
				if D%7==2:
					print("Friday")
				elif D%7==3:
					print("Saturday")
				elif D%7==4:
					print("Sunday")
				elif D%7==5:
					print("Monday")
				elif D%7==6:
					print("Tuesday")
				elif D%7==0:
					print("Wednesday")
				elif D%7==1:
					print("Thursday")
			elif M==5:
				if D%7==6:
					print("Friday")
				elif D%7==0:
					print("Saturday")
				elif D%7==1:
					print("Sunday")
				elif D%7==2:
					print("Monday")
				elif D%7==3:
					print("Tuesday")
				elif D%7==4:
					print("Wednesday")
				elif D%7==5:
					print("Thursday")
			elif M==7 or M==4:
				if D%7==1:
					print("Friday")
				elif D%7==2:
					print("Saturday")
				elif D%7==3:
					print("Sunday")
				elif D%7==4:
					print("Monday")
				elif D%7==5:
					print("Tuesday")
				elif D%7==6:
					print("Wednesday")
				elif D%7==0:
					print("Thursday")
			elif M==11:
				if D%7==4:
					print("Friday")
				elif D%7==5:
					print("Saturday")
				elif D%7==6:
					print("Sunday")
				elif D%7==0:
					print("Monday")
				elif D%7==1:
					print("Tuesday")
				elif D%7==2:
					print("Wednesday")
				elif D%7==3:
					print("Thursday")		
			elif M==1 or M==9 or M==10:
				if D%7==0:
					print("Friday")
				elif D%7==1:
					print("Saturday")
				elif D%7==2:
					print("Sunday")
				elif D%7==3:
					print("Monday")
				elif D%7==4:
					print("Tuesday")
				elif D%7==5:
					print("Wednesday")
				elif D%7==6:
					print("Thursday")
			elif M==6:
				if D%7==3:
					print("Friday")
				elif D%7==4:
					print("Saturday")
				elif D%7==5:
					print("Sunday")
				elif D%7==6:
					print("Monday")
				elif D%7==0:
					print("Tuesday")
				elif D%7==1:
					print("Wednesday")
				elif D%7==2:
					print("Thursday")
			elif M==8:
				if D%7==5:
					print("Friday")
				elif D%7==6:
					print("Saturday")
				elif D%7==0:
					print("Sunday")
				elif D%7==1:
					print("Monday")
				elif D%7==2:
					print("Tuesday")
				elif D%7==3:
					print("Wednesday")
				elif D%7==4:
					print("Thursday")
	except EOFError:
		break