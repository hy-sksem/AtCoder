// https://atcoder.jp/contests/abc193/tasks/abc193_a

#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i, s, n) for (int i = (s); i < (int)(n); i++)
 
int main() {
    double A, B; cin >> A >> B;
    cout << (1 - (B / A)) * 100 << endl;
}