#include<iostream>
#include<vector>
#include<algorithm>
#include<cctype>
using namespace std;
bool compare(const vector<string>& a, const vector<string>& b) {
    return a[0] < b[0];
}

bool compare1(const vector<string>& a, const vector<string>& b) {
    return stoi(a[1]) < stoi(b[1]);
}
int main(){
    int n;
    while(cin>>n){
        string input;
        vector<string> strs;
        for(int i=0;i<n;i++){
            getline(cin,input);
            for(int j=0;j<input.size();j++){
                if(input[j].isaplha()){
                    input[j]=toupper(input[j]);
                    strs.push_back(input[j]);
                }
            }
        }
        vector<vector<string>> ans;
        vector<string> w;
        for(int i=0;i<strs.size();i++){
            vector<stirng> temp;
            if(i==0 | find(w.begin(),w.end(),strs[i])==0){
                temp.push_back(strs[i]);
                temp.push_back(count(strs.begin(),strs.end(),strs[i]));
                w.push_back(strs[i]);
            }
            ans.push_back(temp);
        }
        sort(ans.begin(),ans.end(),compare1);
        reverse(ans.begin(),ans.end());
        sort(ans.begin(),ans.end(),compare);
        for(int i=0;i<ans,size();i++)
            cout << ans[i][0] << " " << ans[i][1] << '\n';
        w.clear();
        ans.clear();
        temp.clear();
    }
    return 0;
}