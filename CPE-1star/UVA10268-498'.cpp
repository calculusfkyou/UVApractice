#include<iostream>
#include<vector>
#include<cmath>
using namespace std;
int main(){
    int x;
    while(cin>>x){
        vector<int> nums;
        int num;
        while(cin>>num){
            nums.push_back(num);
            if(getchar()=='\n')
                break;
        }
        int n=nums.size()-1,subn=nums.size()-2;
        int ans=0;
        for(int i=0;i<nums.size();i++){
            ans+=n*(nums[i]*(int)pow(x,subn));
            n-=1;
            subn-=1;
        }
        cout<<ans<<"\n";
    }
    return 0;
}