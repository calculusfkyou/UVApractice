#include<iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(){
    long long n;
    int sequence=1;
    while(cin>>n){
        vector<string> temp;
        if(n==0)
            temp.push_back("0");
        else{
            int temp2;
            while(n>0){
                temp2=n%100;
                if(temp2!=0)
                    temp.push_back(to_string(temp2));
                n=n/100;
                if(n==0)
                    break;
                temp2=n%10;
                if(temp2!=0){
                    temp.push_back("shata");
                    temp.push_back(to_string(temp2));
                }
                n=n/10;
                if(n==0)
                    break;
                temp2=n%100;	
				if(temp2!=0){
					temp.push_back("hajar");
					temp.push_back(to_string(temp2));
                }
				n=n/100;
				if(n==0)
					break;	
				temp2=n%100;
				if(temp2!=0){
					temp.push_back("lakh");
					temp.push_back(to_string(temp2));
                }
				n=n/100;
				if(n==0)
					break;
				if(n!=0)
				    temp.push_back("kuti");
            }
        }
        reverse(temp.begin(),temp.end());
        if(sequence<10)
            cout<<"   "<<sequence<<". ";
        else    
            cout<<"  "<<sequence<<". ";
        sequence+=1;
        for(int i=0;i<temp.size()-1;i++)
            cout<<temp[i]<<" ";
        cout<<temp.back()<<"\n";
    }
    return 0;
}