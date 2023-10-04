def main():
    n=int(input())
    data=""
    for i in range(n):
        case=input().strip()
        case=case.upper()
        case=case.split()
        case="".join(case)
        data+=case
    ans=[]
    temp=[]
    for i in range(len(data)):
        if data[i].isalpha():
            if data[i] not in temp:
                temp.append(data[i])
                ans.append([data[i],1])
            else:
                for j in range(len(ans)):
                    if ans[j][0]==data[i]:
                        ans[j][1]+=1
    ans.sort(key=lambda ans:ans[0])
    ans.sort(key=lambda ans:ans[1],reverse=1)
    for i in range(len(ans)):
        print(*ans[i])
if __name__=="__main__":
    main()