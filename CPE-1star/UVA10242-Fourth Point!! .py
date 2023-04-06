#這是猜到的寫法，但答案對了，可是暗中測資不給過
while True:
	try:
		nums=list(map(float,input().split()))
		print("%.3f"%(nums[0]+nums[-2]-nums[2]),end=" ")
		print("%.3f"%(nums[1]+nums[-1]-nums[3]))
	except EOFError:
		break

#GPT寫的
while True:
    try:
        nums = list(map(float, input().split()))
        x1, y1, x2, y2, x3, y3, x4, y4 = nums
        if x1 == x3 and y1 == y3:
            print("%.3f %.3f" % (x2 + x4 - x3, y2 + y4 - y3))
        elif x1 == x4 and y1 == y4:
            print("%.3f %.3f" % (x2 + x3 - x4, y2 + y3 - y4))
        elif x2 == x3 and y2 == y3:
            print("%.3f %.3f" % (x1 + x4 - x3, y1 + y4 - y3))
        else:
            print("%.3f %.3f" % (x1 + x3 - x4, y1 + y3 - y4))
    except EOFError:
        break