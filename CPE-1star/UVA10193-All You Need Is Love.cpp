#include <iostream>
#include<cmath>
using namespace std;
int gcd(int a,int b){
    if(a==0 & b!=0)
        return a;
    if(b==0)
        return a;
    else
        return gcd(b,a%b);
}
int main()
{
    int n,no=1;
    while(cin>>n){
        for(int i=0;i<n;i++){
            long long a,b,m;
            cin>>a;
            cin>>b;
            long long bs=0,bs1=0,bs2=0;
            while(a>0){
                bs1+=(a%10)*(int)pow(2,bs);
                a=a/10;
                bs+=1;
            }
            bs=0;
            while(b>0){
                bs2+=(b%10)*(int)pow(2,bs);
                b=b/10;
                bs+=1;
            }
            m=gcd(bs1,bs2);
            if(m!=1)
                cout<<"Pair #"<<no<<": All you need is love!"<<'\n';
            else    
                cout<<"Pair #"<<no<<": Love is not all you need!"<<'\n';
            no+=1;
        }
    }
    return 0;
}
