#印出色骰子上面是甚麼數字，dice[1]上方，dice[2]北方，dice[3]西方，dice[4]東方，dice[5]南方，dice[6]下方
num,dice=0,[0,1,2,3,4,5,6]
while True:
	try:
		n=int(input())
		if n!=0:
			for i in range(1,n+1):
				act=input()
				if act=="east":
					num=dice[4]
					dice[4]=dice[1]
					dice[1]=dice[3]
					dice[3]=dice[6]
					dice[6]=num
				if act=="south":
					num=dice[5]
					dice[5]=dice[1]
					dice[1]=dice[2]
					dice[2]=dice[6]
					dice[6]=num
				if act=="west":
					num=dice[3]
					dice[3]=dice[1]
					dice[1]=dice[4]
					dice[4]=dice[6]
					dice[6]=num
				if act=="north":
					num=dice[2]
					dice[2]=dice[1]
					dice[1]=dice[5]
					dice[5]=dice[6]
					dice[6]=num
			print(dice[1])
			num,dice=0,[0,1,2,3,4,5,6]
	except:
		break