d = {}
d_inverse = {}

def inverse(d):
    return {value : key for key, value in d}

n = int(input())

for i in range(n):
    s = input().split()
    name, tel = ' '.join(s[:2]), s[2]
    d[name] = tel
    d_inverse[tel] = name

m = int(input())

for i in range(m):
    s = input()
    ans = 'Not found'
    if s in d.keys():
        ans = d[s]
    if s in d_inverse.keys():
        ans = d_inverse[s]
    print(s + ' --> ' + ans)