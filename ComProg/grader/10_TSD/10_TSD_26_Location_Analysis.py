d = dict()
name_list = list()

n = int(input())

for i in range(n):
    name, cities = input().split(': ')
    cities = cities.split(', ')
    cities = set(cities)
    name_list.append(name)
    d[name] = cities

ans = list()

keyID = input()

for name in name_list:
    if keyID == name:
        continue
    if len(set.intersection(d[keyID], d[name])):
        ans.append(name)

if len(ans) == 0:
    print('Not Found')

print(*ans, sep = '\n')