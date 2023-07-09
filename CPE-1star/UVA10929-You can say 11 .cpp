//這題不會用C++寫，因為測資超過long long 的範圍
#include<iostream>
using namespace std;
int main(){
    long long n;
    while(cin>>n){
        if(n==0)
            break;
        if(n%11==0)
            cout<<n<<" is a multiple of 11."<<'\n';
        else 
            cout<<n<<" is not a multiple of 11."<<'\n';
    }
    return 0;
}