#include<iostream>
using namespace std;
int gcd(int a,int b){
    if(a==0 & b!=0)
        return a;
    if(b==0)
        return a;
    else
        return gcd(b,a%b);
}
int main(){
    int n;
    while(cin>>n){
        if(n==0)
            break;
        int g=0;
        for(int i=1;i<n;i++)
            for(int j=i+1;j<=n;j++)
                g+=gcd(i,j);
        cout<<g<<'\n';
    }
    return 0;
}