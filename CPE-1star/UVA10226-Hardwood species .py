# 計算每個輸入出現的概率，並用name的ascii大小印出
while True:
	try:
		n=int(input())
		for k in range(n):
			if k==0:#注意這該死的空格，只會輸入一次
				space=input()
			trees=[]
			#print(space)
			while True:
				try:
					tree=input()
					if tree=="":
						break
					trees.append(tree)
				except:
					break
			#print(trees)
			ans=[]
			temp=[]
			for i in range(len(trees)):
				if trees[i] not in temp:
					temp.append(trees[i])
					count=trees.count(trees[i])
					ans.append([trees[i],count/len(trees)*100])
			ans.sort(key=lambda ans:ans[0])
			for i in range(len(ans)-1):
				print("%s %.4f"%(ans[i][0],ans[i][1]))
			print("%s %.4f"%(ans[-1][0],ans[-1][1]))
			if k!=n-1:
				print()
	except EOFError:
		break