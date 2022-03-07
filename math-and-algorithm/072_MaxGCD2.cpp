#include <iostream>
using namespace std;

int A, B, ans = 0;

bool check(int t) {
    int cl = (A+t-1)/t;
    int cr = B/t;
    if (cr-cl>=1) return true;
    return false;
}

int main() {
    cin >> A >> B;
    for (int i=1; i<=B; i++) {
        if (check(i)) ans = i;
    }
    cout << ans << endl;
    return 0;
}
