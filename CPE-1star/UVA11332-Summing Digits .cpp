#include<iostream>
using namespace std;
int main(){
    int n;
    while(cin>>n){
        if(n==0)
            break;
        int temp=0;
        while(n>=10){
            while(n>0){
                temp+=n%10;
                n=n/10;
            }
            n=temp;
            temp=0;
        }
        cout<<n<<'\n';
    }
    return 0;
}