#include<iostream>
using namespace std;
int main(){
    int n;
    while(cin>>n){
        for(int i=0;i<n;i++){
            int num;
            cin>>num;
            int bs=0,hm=0,count=0,subm=num;
            while(subm>0){
                if(subm%2==1)
                    count+=1;
                subm=subm/2;
            }
            cout<<count<<" ";
            count=0;
            while(num>0){
                int temp=num%10;
                while(temp>0){
                    if(temp%2==1)
                        count+=1;
                    temp=temp/2;
                }
                num=num/10;
            }
            cout<<count<<'\n';
        }
    }
    return 0;
}