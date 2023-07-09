#include<iostream>
using namespace std;
int main(){
    long long n;
    while(cin>>n){
        if(n==0)
            break;
        if(n%9!=0)
            cout<<n<<" is not a multiple of 9."<<"\n";
        else{
            int temp=0,subn=n,degree=0;
            while(subn%9==0){
                while(subn>0){
                    temp+=subn%10;
                    subn=subn/10;
                }
                if(temp%9==0)
                    degree+=1;
                subn=temp;
                temp=0;
                if(subn==9)
                    break;
            }
            cout<<n<<" is a multiple of 9 and has 9-degree "<<degree<<"."<<'\n';
        }
    }
    return 0;
}