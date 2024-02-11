#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    int n, a;
    cin >> n >> a;
    vector <int> t(n);
    for(int i = 0; i < n; i++) {
        cin >> t[i];
    }
    while(a--) {
        long long c;
        cin >> c;
        long long l = 0, r = 1e12;
        while(l < r) {
            long long mid = (l + r) / 2;
            long long sum = n;
            for(int i = 0; i < n; i++) {
                sum += mid / t[i];
            }
            if(sum >= c) {
                r = mid;
            }
            else {
                l = mid + 1;
            }
        }
        cout << l << '\n';
    }
    return 0;
}

/*
3 5
2 2 5
4 5 6 30 123456789012
*/