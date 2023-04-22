sentences=[]
#處理輸入，可能有很多行
while True:
	try:
		s=input()
		sentences.append(s)
	except EOFError:
		break
#將好幾列字串90度轉過來 一列一列輸出
s_long=len(sentences)
longest=len(sentences[0])
for i in range(len(sentences)):
	if len(sentences[i])>longest:
		longest=len(sentences[i])
		
temp=[[""]*s_long for i in range(longest)]
for i in range(len(sentences)-1,-1,-1):
	subsen=sentences[i]
	for j in range(len(subsen)):
		temp[j][i]=subsen[j]
#print(temp)
count=0#計算超過字串長度的部分
for i in range(len(temp)):
	for j in range(len(temp[i])-1,0,-1):
		if temp[i][j]=="":#字串如果已超出範圍則會抓到""，就需要加入計算
			count+=1
		elif count!=0:
			for z in range(count):
				print(" ",end="")#如果找到還有字元的長度，確認前面有沒有空格(已經超過字串範圍的格子)
                                 #再將它輸出
			count=0
			print(temp[i][j],end="")
		else:
			print(temp[i][j],end="")
	print(temp[i][0])