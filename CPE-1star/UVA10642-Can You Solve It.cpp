#include <iostream>
using namespace std;
int location(int x,int y){
    return (x+y)*(x+y+1)/2+x;
}
int main()
{
    int n,count=1;
    while(cin>>n){
        for(int i=0;i<n;i++){
            int x1,y1,x2,y2;
            cin>>x1>>y1>>x2>>y2;
            cout<<"Case "<<count<<": "<<location(x2,y2)-location(x1,y1)<<'\n';
            count+=1;
        }
    }
    return 0;
}
