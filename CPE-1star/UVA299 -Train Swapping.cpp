#include<iostream>
#include <vector>
using namespace std;
int bbsort(vector<int>& subnum){
    int count=0;
    for(int k=0;k<subnum.size()-1;k++)
        for(int j=0;j<subnum.size()-1;j++){
            if(subnum[j]>subnum[j+1]){
                int temp=subnum[j+1];
                subnum[j+1]=subnum[j];
                subnum[j]=temp;
                count+=1;
            }
        }
    return count;
}
int main(){
    int n;
    while(cin>>n){
        for(int i=0;i<n;i++){
            int l;
            cin>>l;
            vector<int> nums(l);
            for(int j=0;j<l;j++){
                int num;
                cin>>num;
                nums[j]=num;
            }
            cout<<"Optimal train swapping takes "<<bbsort(nums)<<" swaps."<<"\n";
        }
    }
    return 0;
}