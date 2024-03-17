# 找到最小進為花費，若有相同的，則也印出，建議收看: https://www.youtube.com/watch?v=z8cM3pTXqUI
# v1
case = 1
n = int(input())
for c in range(n):
    try:
        print("Case %d:" % (case))
        cost = []
        for i in range(4):
            num = list(map(int, input().split()))
            cost.extend(num)
        line = int(input())
        for i in range(line):
            x = int(input())
            cost2 = []
            for base in range(2, 37):
                total = 0
                temp = x
                while temp > 0:
                    re = temp % base
                    total = total + cost[re]
                    temp = temp // base
                cost2.append([base, total])
            cost2.sort(key=lambda cost2: cost2[1])
            print("Cheapest base(s) for number %d:" % (x), end="")
            minimum = cost2[0][1]
            for base in range(len(cost2)):
                if cost2[base][1] == minimum:
                    print(" %d" % (cost2[base][0]), end="")
                else:
                    break
            print()
        if case < n:
            print()
        case += 1
    except EOFError:
        break

# v2
t = int(input())
for i in range(t):
    print("Case " + str(i + 1) + ":")
    cost= []
    for j in range(4):
        cost.extend(map(int, input().split()))
    for k in range(int(input())):
        num = int(input())
        m = []
        minimum = 1000000000000000000000
        for base in range(2, 37):
            total = 0
            temp = num
            while temp > 0:
                total += cost[temp % base]
                temp //= base
            if total <= minimum:
                minimum = total
                m.append([base, total])
        m.sort(key=lambda m: m[1])
        temp = []
        for l in m:
            if l[1] == minimum:
                temp.append(l[0])
        print("Cheapest base(s) for number %d: " % num, end="")
        print(*temp)
    if i != (t - 1):
        print()
