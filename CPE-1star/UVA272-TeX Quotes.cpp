#include <iostream>
#include <vector>
using namespace std;

int main() {
    string text;
    vector<string> strs;
    int count = 0;
    while (getline(cin, text)) {
        strs.push_back(text);
    }
    for (int i = 0; i < strs.size(); i++) {
        string line = strs[i];
        for (int j = 0; j < line.size(); j++) {
            if (line[j] == '"') {
                if (count % 2 == 0)
                    cout << "``";
                else
                    cout << "''";
                count += 1;
            }
            else
                cout << line[j];
        }
        cout << endl;
    }
    return 0;
}
