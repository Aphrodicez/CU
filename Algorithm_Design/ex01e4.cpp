#include <bits/stdc++.h>
using namespace std;

long long modexpo(long long a, long long n, long long MOD) {
    if(n == 0) {
        return 1ll % MOD;
    }
    if(n == 1) {
        return a % MOD;
    }
    long long half = modexpo(a, n / 2, MOD);
    if(n & 1) {
        return (((half * half) % MOD) * a) % MOD;
    }
    else {
        return (half * half) % MOD;
    }
}

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    long long a, n, MOD;
    cin >> a >> n >> MOD;
    cout << modexpo(a, n, MOD);
    return 0;
}

/*
123 4727 153
*/