check=1
while True:
	try:
		text=list(input())
		if check:
			check=0
		else:
			print()
		temp=[]
		used=[]
		for i in range(len(text)):
			a=0
			if text[i] not in used:
				used.append(text[i])
				a=text.count(text[i])
				temp.append([ord(text[i]),a])
		temp.sort(key=lambda temp:(temp[0]),reverse=1)
		temp.sort(key=lambda temp:(temp[1]))
		for i in range(len(temp)):
			print(temp[i][0],end=" ")
			print(temp[i][1])
	except EOFError:
		break
