#瘋狂程設通過，UVA 超時不通過
def sum_of_digits(s):
    total = 0
    for char in s:
        if char.isdigit():  
            total += int(char)  
    return total
    
t=int(input())
for i in range(t):
	n=int(input())
	check=0
	for j in range(n):
		if (j+sum_of_digits(str(j)))==n:
			print(j)
			check=1
			break
	if not check:
		print(0)