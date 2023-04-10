#計算出day天內因為罷會損失多少工作天。星期五和六為假日不算，政黨間的罷會天重複只算一次
while True:
    try:
        case = int(input())
        for i in range(case):
            day = int(input())
            p = int(input())
            hartal = []
            for j in range(p):#有多少政黨的罷會週期
                h = int(input())#幾天罷一次
                for k in range(1, day+1):#倍數存取，不大於所給天數
                    if h*k > day:
                        break
                    else:
                        hartal.append(h*k)
            count = 0

            temp = []
            for l in range(len(hartal)):
                same = hartal.count(hartal[l])#這行沒必要     
                if hartal[l] not in temp:#只收不一樣的日子
                    temp.append(hartal[l])

            for a in temp:
                if a % 7 != 0 and a % 7 != 6:#排除星期五，星期六
                    count += 1
            print(count)
    except EOFError:
        break