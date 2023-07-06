sentences=[]
while True:
	try:
		s=input()
		sentences.append(s)
	except EOFError:
		break
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
count=0	
for i in range(len(temp)):
	for j in range(len(temp[i])-1,0,-1):
		if temp[i][j]=="":
			count+=1
		elif count!=0:
			for z in range(count):
				print(" ",end="")
			count=0
			print(temp[i][j],end="")
		else:
			print(temp[i][j],end="")
	print(temp[i][0])