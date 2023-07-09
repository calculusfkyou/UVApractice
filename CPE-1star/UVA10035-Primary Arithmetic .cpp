#include <iostream>
using namespace std;

int main() {
    while (true) {
        int n, m;
        cin >> n >> m;
        if (n == 0 && m == 0) {
            break;
        }

        int carry = 0;
        int carryDigit = 0;
        while (n > 0 || m > 0) {
            int digitSum = (n % 10) + (m % 10) + carryDigit;
            if (digitSum >= 10) {
                carry++;
                carryDigit = 1;
            } else {
                carryDigit = 0;
            }
            n /= 10;
            m /= 10;
        }

        if (carry == 0) {
            cout << "No carry operation." << endl;
        } else if (carry == 1) {
            cout << "1 carry operation." << endl;
        } else {
            cout << carry << " carry operations." << endl;
        }
    }

    return 0;
}
