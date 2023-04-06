#我用二維陣列
#你要依照某些規則排序N個整數。先利用每個數字除以M的餘數由小到大排，若排序中比較的兩數為一奇一偶且兩數除以M的餘數相等，則奇數要排在偶數前面。
#若兩奇數除以M餘數大小相等，則原本數值較大的奇數排在前面。
#若兩偶數除以M餘數大小相等，則較小的偶數排在前面。
while True:
	try:
		n,m=map(int,input().split())
		if n==0 and m==0:
			break
		nums=[]
		for i in range(n):
			num=int(input())
			if num>0:
				nums.append([num,num%m])
			else:
				nums.append([num,-(abs(num)%m)])#負數的餘數
		o,O=map(int,input().split())#0 0
		temp=[]
		for i in range(len(nums)):#奇數
			if nums[i][0]%2!=0:
				temp.append(nums[i])
		temp.sort(key=lambda temp:temp[0],reverse=1)#讓奇數由大到小排
		temp2=[]
		for i in range(len(nums)):#偶數
			if nums[i][0]%2==0:
				temp2.append(nums[i])
		temp2.sort(key=lambda temp:temp[0])#讓偶數由小到大排
		nums=temp[:]+temp2[:]#奇數+偶數，達到奇數再偶數前面
		nums.sort(key=lambda nums:(nums[1]))#最後以餘數大小排列
		print(n,end=" ")
		print(m)
		for i in range(len(nums)):
			print(nums[i][0])
		print(0,end=" ")
		print(0)
	except:
		break