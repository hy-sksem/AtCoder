#include <iostream>
using namespace std;

long long N, ans = 0;

int main() {
    cin >> N;
    ans += (N / 10000); N %= 10000;
    ans += (N / 5000); N %= 5000;
    ans += (N / 1000); N %= 1000;
    cout << ans << endl;
    return 0;
}
