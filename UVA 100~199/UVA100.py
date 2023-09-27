# runtime error
while True:
    try:
        n,m=map(int,input().split())
        print("%d %d"%(n,m),end=" ")
        if n>m:
            n,m=m,n
        s=[]
        for i in range(n,m+1):
            temp=[]
            if i==1:
                pass
            else:
                temp.append(i)
                sub=i
                while True:
                    if sub==1:
                        break
                    else:
                        if sub%2!=0: 
                            sub=sub*3+1
                        else:
                            sub=sub//2
                        temp.append(sub)
                s.append(len(temp))
        print(max(s))
        s.clear()
    except EOFError:
        break