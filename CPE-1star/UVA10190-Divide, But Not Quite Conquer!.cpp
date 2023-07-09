#include<vector>
#include<iostream>
using namespace std;
int main(){
    int a,b;
    while(cin>>a>>b){
        if(a!=1 & b!=1){
            vector<int> nums;
            nums.push_back(a);
            while(a>1 & a%b==0){
                a=a/b;
                nums.push_back(a);
            }
            if(nums.back()!=1)
                cout<<"Boring!";
            if(nums.back()==1){
                for(int i=0;i<nums.size();i++){
                    if(nums[i]!=1)
                        cout<<nums[i]<<" ";
                    if(nums[i]==1)
                        cout<<nums[i];
                }
            }
        }
        else    
            cout<<"Boring!";
    	cout<<'\n';
    }
    return 0;
}