#include <iostream>
using namespace std;

long long N, A[200009], ans = 0;

int main() {
    cin >> N;
    for (int i = 1; i <= N; i++) cin >> A[i];

    for (int i = 1; i <= N; i++) {
        ans += A[i] * (-N + 2LL * i - 1LL);
    }
    cout << ans << endl;
    return 0;
}
