#輸出以出現次數優先，小到大排序，若有相同，再以ascii大小排序
#每組輸出空一行，最後一組不空
#我用二維陣列，chr(數字)=ascii文字，ord(ascii文字)=數字
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
