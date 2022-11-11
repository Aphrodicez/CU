def sign(n):
    if n > 0:
        return '+' + str(n)

    return str(n)

def diff(l, r):
    # diff = difference
    if l[0] != r[0]:
        return sign(d[l[0]] - d[r[0]])
    
    return sign(d[l[1]] - d[r[1]])

s = input()

values = 'A23456789TJQK'
suits = 'CDHS'

d = dict()

for i in range(len(values)):
    d[values[i]] = i + 1

for i in range(len(suits)):
    d[suits[i]] = i + 1

a = [s[i : i + 2] for i in range(0, len(s), 2)]
ans = ''

for i in range(len(a) - 1):
    ans += diff(a[i], a[i + 1])

print(ans)