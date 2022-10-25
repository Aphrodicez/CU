from unicodedata import name


sz = {}

n = int(input())
for i in range(n):
    dept, cnt = input().split()
    sz[dept] = int(cnt)

ans = []

m = int(input())
for i in range(m):
    s = input().split()
    ans.append([int(s[0]), float(s[1]), s[2 : ]])

ans = sorted(ans, key = lambda x : x[1], reverse = True)

for x in ans:
    for dept in x[2]:
        if sz[dept] > 0:
            x.append(dept)
            sz[dept] -= 1
            break

ans = sorted(ans, key = lambda x : x[0])

for x in ans:
    print(x[0], x[-1])