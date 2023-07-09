#include <iostream>
#include <bits/stdc++.h>
using namespace std;
 
int main()
{
    int a,b;
    while(cin>>a>>b){
        if(a==0 & b==0)
            break;
        int count=0;
        for(int i=a;i<=b;i++){
            float temp=sqrt(i);
            if((temp-(int)temp)==0)
                count+=1;
        }
        cout<<count<<'\n';
    }
    return 0;
}