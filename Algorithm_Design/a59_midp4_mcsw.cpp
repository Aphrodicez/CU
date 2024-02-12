#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    int n, w;
    cin >> n >> w;
    vector <int> qs(n + 1, 0);
    deque <int> deq;
    deq.push_back(0);
    int mx = -2e9;
    for(int i = 1; i <= n; i++) {
        cin >> qs[i];
        qs[i] += qs[i - 1];
        while(!deq.empty() && i - deq.front() + 1 > w) {
            deq.pop_front();
        }
        mx = max(mx, qs[i] - qs[deq.front()]);
        while(!deq.empty() && qs[deq.back()] >= qs[i]) {
            deq.pop_back();
        }
        deq.push_back(i);
    }
    cout << mx << '\n';
    return 0;
}

/*
10 4 
1 4 2 -3 5 -7 3 9 2 -7
*/