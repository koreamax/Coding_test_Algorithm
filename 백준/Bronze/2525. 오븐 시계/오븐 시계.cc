#include <iostream>

using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b;
    cin >> c;
    b += c;

    while (a >= 24 || b >= 60) {
        if (b >= 60) {
            b -= 60;
            a += 1;
        }
        if (a >= 24) {
            a -= 24;
        }
    }

    cout << a << " " << b << endl;
}