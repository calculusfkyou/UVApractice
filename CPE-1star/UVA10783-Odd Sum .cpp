#include <iostream>
using namespace std;
 
int main()
{
    int n,count=1;
    while(cin>>n){
        int num[2];
        for(int i=0;i<n;i++){
            cin>>num[0];
            cin>>num[1];
            int temp=0;
            for(int j=num[0];j<=num[1];j++)
                if(j%2!=0)
                    temp+=j;
            cout<<"Case "<<count<<": "<<temp<<'\n';
            count+=1;
        }
    }
    return 0;
}
