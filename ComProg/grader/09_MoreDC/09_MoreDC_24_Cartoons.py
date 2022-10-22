d = {}
keys = []

while True:
    s = input()
    if s == 'q':
        break
    s = s.split(', ')
    if s[1] not in keys:
        keys.append(s[1])
        d[s[1]] = []
    d[s[1]].append(s[0])
        
for key in keys:
    print(key + ': ' + ', '.join(d[key]))