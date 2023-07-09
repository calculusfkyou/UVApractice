#include<iostream>
using namespace std;
int main(){
    long long s,d,ans;
    while(cin>>s>>d){
        while(d>0){
            ans=s;
            d=d-s;
            s+=1;
        }
        cout<<ans<<"\n";
    }
    return 0;
}