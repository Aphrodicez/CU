h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

t1 = h1 * 3600 + m1 * 60 + s1
t2 = h2 * 3600 + m2 * 60 + s2
t = (t2 - t1 + 86400) % 86400
print(t // 3600, (t // 60) % 60, t % 60, sep = ':')