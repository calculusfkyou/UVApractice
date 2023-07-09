#include <iostream>
#include<vector>
using namespace std;
 
int main()
{
    int n,num=0;
    vector<int> dice={0,1,2,3,4,5,6};
    while(cin>>n){
        if(n!=0){
            for(int i=1;i<n+1;i++){
                string act;
                cin>>act;
                if(act=="east"){
                    num=dice[4];
					dice[4]=dice[1];
					dice[1]=dice[3];
					dice[3]=dice[6];
					dice[6]=num;
                }
                if(act=="south"){
					num=dice[5];
					dice[5]=dice[1];
					dice[1]=dice[2];
					dice[2]=dice[6];
					dice[6]=num;
                }
				if(act=="west"){
					num=dice[3];
					dice[3]=dice[1];
					dice[1]=dice[4];
					dice[4]=dice[6];
					dice[6]=num;
                }
				if(act=="north"){
					num=dice[2];
					dice[2]=dice[1];
					dice[1]=dice[5];
					dice[5]=dice[6];
					dice[6]=num;
                }
            }
			cout<<dice[1]<<'\n';
			num=0,dice={0,1,2,3,4,5,6};
        }
        else    
            break;
    }
    return 0;
}
