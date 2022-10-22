n = int(input())

if n == 0:
    print(0)
    print(0)
    exit()

a = []

for i in range(n):
    s = set([int(x) for x in input().split()])
    a.append(s)

print(len(set.union(*a)))
print(len(set.intersection(*a)))