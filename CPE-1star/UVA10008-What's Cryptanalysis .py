while True:
    try:
        n=int(input())
        temp=[]
        ans=[]
        subs=""
        for i in range(n):
            s=input()
            s=s.upper()
            subs+=s
        for j in range(len(subs)):
            if subs[j] not in temp and subs[j].isalpha():
                count=subs.count(subs[j])
                temp.append(subs[j])
                ans.append([subs[j],count])
        ans.sort(key=lambda ans:ans[0])
        ans.sort(key=lambda ans:int(ans[1]),reverse=1)
        for i in range(len(ans)-1):
            print(*ans[i])
        print(*ans[-1])
    except:
        break