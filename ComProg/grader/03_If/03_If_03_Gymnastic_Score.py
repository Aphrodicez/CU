s = [float(x) for x in input().split()]

ans = sum(s)
mn = mx = s[0]

for x in s:
    if mn > x:
        mn = x
    if mx < x:
        mx = x

print(round((sum(s) - (mn + mx)) / (len(s) - 2), 2))