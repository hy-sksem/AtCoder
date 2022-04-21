// https://atcoder.jp/contests/abc131/tasks/abc131_b

#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)
 
int main() {
    int N, L; cin >> N >> L;
    int ans = 0, min = 1000;
    rep2(i, 1, N+1) {
        ans += L + i - 1;
        if (abs(L + i - 1) < abs(min)) {
            min = L + i - 1;
        }
    }
    cout << ans - min << endl;
}