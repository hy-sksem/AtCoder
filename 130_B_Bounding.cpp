// https://atcoder.jp/contests/abc130/tasks/abc130_b

#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)

int main() {
    int N, X; cin >> N >> X;
    int cnt;
    vector<int> L(N);
    rep(i, N) {
        cin >> L.at(i);
    }
    rep2(j, 1, N+1) {
        cnt += L.at(j-1);
        if (cnt == X) {
            cout << j+1 << endl;
            return 0;
        }
        else if (cnt > X) {
            cout << j << endl;
            return 0;
        }
        else {
            continue;
        }
    }
    cout << N+1 << endl;

}
