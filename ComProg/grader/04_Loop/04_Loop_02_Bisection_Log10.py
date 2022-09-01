a = float(input())
l = 0
r = a

while l < r:
    mid = (l + r) / 2
    val = 10 ** mid
    if abs(a - val) <= (10 ** -10) * max(a, val):
        l = mid = r
    elif val > a:
        r = mid
    else:
        l = mid

print(round(l, 6))