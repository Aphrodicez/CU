d = dict()
ans = dict()

q = int(input())

for t in range(1, q + 1):
    s = input().split()
    if s[0] == 'B':
        b, p, w = s[1:]
        if p not in d:
            d[p] = dict()
        if b not in d[p]:
            d[p][b] = dict()
        d[p][b] = (w, -t)
    elif s[0] == 'W':
        b, p, = s[1:]
        if p in d and b in d[p]:
            d[p].pop(b)
    
    if b not in ans:
        ans[b] = list()

    q -= 1

for p in d.keys():
    b_list = []
    for b in d[p].keys():
        b_list.append((d[p][b], b))
    if len(b_list) == 0:
        continue
    w, b = sorted(b_list, reverse = True)[0]
    ans[b].append((p, w))

for b in sorted(ans.keys()):
    s = b + ': $' + str(0 + sum(int(x[1][0]) for x in ans[b]))
    if len(ans[b]) > 0:
        s += ' ->'
    for (p, w) in sorted(ans[b]):
        s += ' ' + p
    print(s)