// https://atcoder.jp/contests/abc193/tasks/abc193_b

#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)
 
int main() {
    int N; cin >> N;
    int ans = 2000000000;
    bool flag = false;
    rep(i, N) {
        int A, P, X; cin >> A >> P >> X;
        if (X - A > 0 && P < ans) {
            ans = P;
            flag = true;
        }
    }
    if (flag) {
        cout << ans << endl;    
    }
    else {
        cout << -1 << endl;
    }
}