#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    vector <long long> a(1000000);
    vector <long long> qs(1000000);
    int i = 3, now = 2, cnt = 1;
    a[1] = 1;
    a[2] = 2;
    qs[1] = a[1];
    qs[2] = qs[2 - 1] + a[2];
    for(; ; i++) {
        a[i] = now;
        cnt--;
        if(cnt == 0) {
            now++;
            cnt = a[now];
        }
        qs[i] = qs[i - 1] + a[i];
        if(qs[i] > 2000000000) {
            break;
        }
    }
    qs.resize(i + 1);
    int n;
    cin >> n;
    while(n--) {
        long long x;
        cin >> x;
        cout << lower_bound(qs.begin(), qs.end(), x) - qs.begin() << '\n';
    }
    return 0;
}

/*
4
100
9999
123456
1000000000
*/