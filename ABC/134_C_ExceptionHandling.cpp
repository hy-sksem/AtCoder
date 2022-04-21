// https://atcoder.jp/contests/abc134/tasks/abc134_c

#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    int max = 0;
    int second = 0;
    bool duplicate = false;
    for (int i = 0; i < N; i++){
        cin >> A.at(i);
        int a;
        a = A.at(i);
        if (a > max){
            second = max;
            max = a;
            duplicate = false;
        }
        else if (a == max){
            duplicate = true;
        }
        else if (a > second) {
            second = a;
        }
    }
    for (int i = 0; i < N; i++){
        int b;
        b = A.at(i);
        if (b < max){
            cout << max << endl;
        }
        else if (b == max && duplicate){
            cout << b << endl;
        }
        else {
            cout << second << endl;
        }
    }
}
