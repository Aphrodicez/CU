# adj = adjacent stations

adj = dict()

st = ''

while True:
    s = input().split()
    
    if len(s) == 1:
        st = ''.join(s)

        if st not in adj:
            adj[st] = list()

        break
    
    u, v = s
    
    if u not in adj:
        adj[u] = list()
    
    if v not in adj:
        adj[v] = list()

    adj[u].append(v)
    adj[v].append(u)

ans = set()

ans.add(st)

for x in adj[st]:
    ans.add(x)

    for y in adj[x]:
        ans.add(y)

print(*sorted(ans), sep = '\n')