#include <iostream>
#include <cmath>
#include <string>
using namespace std;
int main() {
    double s = 0, distance = 0;
    int r, degree;
    string unit;
    while(cin>>r>>degree>>unit){
        if (unit == "min")
            degree /= 60;
        s = 2 * M_PI * (r + 6440) * (degree / 360);
        distance = 2 * (r + 6440) * sin(degree * M_PI / 180 / 2);
        cout << fixed;
        cout.precision(6);
        cout << round(s * 1000000) / 1000000 << " " << round(distance * 1000000) / 1000000 << std::endl;
        s = 0;
        distance = 0;
    }
    return 0;
}