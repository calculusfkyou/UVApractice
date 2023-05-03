#include<bits/stdc++.h>
using namespace std;
int main(){
    int I,J;
    while(cin>>I>>J){
        cout<<I<<" "<<J<<" ";
        int count=1;
        int temp=1;
        if(I!=J){
        	if(I>J){
                swap(I,J);
        	}
            for(int i=I;i<=J;i++){
                int cur=i;
                while(cur!=1){
                    if(cur%2!=0)
                        cur=3*cur+1;
                    else
                        cur=cur/2;
                    temp+=1;
                }
                if(temp>=count)
                    count=temp;
                temp=1;
            }
        }
        else if(I==J){
            while(I!=1){
                if(I%2!=0)
                    I=3*I+1;
                else
                    I=I/2;
                count+=1;
            }
        }
        cout<<count<<"\n";
    }
    return 0;
}