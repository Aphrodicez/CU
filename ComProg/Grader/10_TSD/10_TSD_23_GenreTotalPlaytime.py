def to_sec(s):
    return 60 * int(s[:-3]) + int(s[-2:])

def to_ms(s):
    return str(s // 60) + ':' + (2 * '0' + str(s % 60))[-2:]

d = dict()

n = int(input())

for i in range(n):
    s = input().strip().split(', ')
    
    if s[-2] not in d:
        d[s[-2]] = 0
    
    d[s[-2]] += to_sec(s[-1])

d = [(key, value) for (key, value) in d.items()]
d = sorted(d, key = lambda x : x[1], reverse = True)

for (key, value) in d[:3]:
    print(key, '-->', to_ms(value))