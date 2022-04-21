// https://atcoder.jp/contests/abc131/tasks/abc131_c

#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)

int main() {
    int64_t A, B, C, D; cin >> A >> B >> C >> D;
    int64_t lc;
    lc = C*D / __gcd(C, D);
    cout << (B - B / C - B / D + B / lc) - ((A-1) - (A-1) / C - (A-1) / D + (A-1) / lc) << endl;
}