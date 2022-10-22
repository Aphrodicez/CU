d_name = {}
d_nickname = {}

n = int(input())

for i in range(n):
    name, nickname = [x.strip() for x in input().split()]
    d_name[name] = nickname
    d_nickname[nickname] = name

m = int(input())

for i in range(m):
    s = input().strip()
    ans = 'Not found'
    if s in d_name.keys():
        ans = d_name[s]
    elif s in d_nickname.keys():
        ans = d_nickname[s]
    print(ans)