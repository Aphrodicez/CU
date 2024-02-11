#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 1e5 + 10;

int a[MAX_N];
int tmp[MAX_N];

long long ans = 0;

void mergeSort(int l, int r) {
    if(l == r) {
        return ;
    }
    int mid = (l + r) / 2;
    mergeSort(l, mid);
    mergeSort(mid + 1, r);
    int i = l, j = mid + 1, k = l;
    while(i <= mid && j <= r) {
        if(a[i] > a[j]) {
            ans += mid - i + 1;
            tmp[k++] = a[j++];
        }
        else {
            tmp[k++] = a[i++];
        }
    }
    while(i <= mid) {
        tmp[k++] = a[i++];
    }
    while(j <= r) {
        tmp[k++] = a[j++];
    }
    for(int i = l; i <= r; i++) {
        a[i] = tmp[i];
    }
}

int main() {
    cin.tie(nullptr)->sync_with_stdio(false);

    int n;
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> a[i];
    }
    mergeSort(0, n - 1);
    cout << ans << '\n';
    return 0;
}

/*
4
10 30 40 20
*/