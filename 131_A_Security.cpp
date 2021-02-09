// https://atcoder.jp/contests/abc131/tasks/abc131_a

#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
 
int main() {
    string S; cin >> S;
    char forward = ' ';
    rep(i,4) {
        if (forward == S.at(i)) {
            cout << "Bad" << endl;
            return 0;
        }
        else {
            forward = S.at(i);
        }
    }
    cout << "Good" << endl;
}