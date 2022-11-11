C = open(input().strip(), 'r').read().split()
L = open(input().strip(), 'r').read()
ans = L
for c in C:
    for w in sorted(set([L[i:i+len(c)] for i in range(len(L)) if L[i:i+len(c)].lower() == c.lower()]))[::-1]: # In Case Replace Color Tag
        ans = ans.replace(w, '<%s>%s</>' % (c.lower(), w))
print(ans)