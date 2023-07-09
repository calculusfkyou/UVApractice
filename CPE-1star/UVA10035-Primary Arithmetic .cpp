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
        while (true) {
            if (n == 0 && m == 0) {
                break;
            }
            if ((n % 10) + (m % 10) >= 10) {
                carry++;
                n = n / 10 + 1;
                m = m / 10;
            } else {
                n = n / 10;
                m = m / 10;
            }
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
