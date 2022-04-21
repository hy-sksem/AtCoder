// https://atcoder.jp/contests/abc132/tasks/abc132_c

#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
 
int main() {
    int n; cin >> n;
    vector<int> d(n);
    rep(i, n) {
        cin >> d[i];
    }
    sort(d.begin(), d.end());
    cout << d.at(n/2) - d.at(n/2-1) << endl;
    return 0;
}
