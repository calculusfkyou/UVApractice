#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    while (cin >> n) {
        vector<int> nums(n);
        for (int i=0;i<n;i++) {
            cin >> nums[i];
        }
        vector<int> temp(n-1);
        for (int i=1; i<n;i++) {
            temp[i-1]=abs(nums[i]-nums[i-1]);
        }
        sort(temp.begin(),temp.end());
        bool isJolly=true;
        for (int i=0; i<n-1;i++) {
            if (temp[i]!=i+1) {
                isJolly=false;
                break;
            }
        }
        if(isJolly){
            cout << "Jolly" << endl;
        } else {
            cout << "Not jolly" << endl;
        }
    }
    return 0;
}
