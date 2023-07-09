#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    while (cin >> n) {
        for (int i = 0; i < n; i++) {
            int m;
            cin >> m;
            vector<int> nums(m);
            for (int j = 0; j < m; j++) {
                cin >> nums[j];
            }
            sort(nums.begin(), nums.end());
            int length = nums.size();
            int mid = nums[length / 2];
            int distance = 0;
            for (int j = 0; j < length; j++) {
                distance += abs(mid - nums[j]);
            }
            cout << distance << "\n";
        }
    }
    return 0;
}
