// https://atcoder.jp/contests/abc132/tasks/abc132_b

#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)
 
int main() {
    int n; cin >> n;
    vector<int> p(n);
    rep(i, n) {
        cin >> p[i];
    }
    int ans = 0;
    rep2(i, 1, n-1) {
        if ((p[i-1] < p[i]) && (p[i] < p[i+1])){
            ans++;
        }
        else if ((p[i-1] > p[i]) && (p[i] > p[i+1])){
            ans++;
        }
    }
    cout << ans << endl;
}