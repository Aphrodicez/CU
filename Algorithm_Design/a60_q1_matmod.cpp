#include <bits/stdc++.h>
using namespace std;


vector <vector <long long>> matrixmul(vector <vector <long long>> &a, vector <vector <long long>> &b, long long MOD) {
    vector <vector <long long>> tmp(2, vector <long long> (2, 0));
    for(int i = 0; i < 2; i++) {
        for(int j = 0; j < 2; j++) {
            for(int k = 0; k < 2; k++) {
                tmp[i][j] = (tmp[i][j] + (a[i][k] * b[k][j]) % MOD) % MOD;
            }
        }
    }
    return tmp;
}

vector <vector <long long>> modexpo(vector <vector <long long>> &a, long long n, long long MOD) {
    if(n == 0) {
        vector <vector <long long>> tmp(2, vector <long long> (2, 0));
        for(int i = 0; i < 2; i++) {
            tmp[i][i] = (1ll % MOD);
        }
        return tmp;
    }
    if(n == 1) {
        for(int i = 0; i < 2; i++) {
            for(int j = 0; j < 2; j++) {
                a[i][j] %= MOD;
            }
        }
        return a;
    }
    vector <vector <long long>> half = modexpo(a, n / 2, MOD);
    vector <vector <long long>> res = matrixmul(half, half, MOD);
    if(n & 1) {
        return matrixmul(a, res, MOD);
    }
    else {
        return res;
    }
}

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    long long n, MOD;
    cin >> n >> MOD;
    vector <vector <long long>> a(2, vector <long long> (2));
    for(int i = 0; i < 2; i++) {
        for(int j = 0; j < 2; j++) {
            cin >> a[i][j];
        }
    }
    vector <vector <long long>> ans = modexpo(a, n, MOD);
    for(int i = 0; i < 2; i++) {
        for(int j = 0; j < 2; j++) {
            cout << ans[i][j] << " ";
        }
    }
    cout << '\n';
    return 0;
}

/*
2 1000
1 2 3 4
*/