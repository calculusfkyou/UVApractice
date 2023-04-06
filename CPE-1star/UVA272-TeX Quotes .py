#第一個"換成``，第二個換成''，以此下去改
count=0
while True:
	try:
		text=input()
		for i in range(len(text)):
			if text[i]=='"':
				if count%2==0:
					print("``",end="")
				else:
					print("''",end="")
				count+=1
			else:
				print(text	[i],end="") 
		print()
	except EOFError:
		break