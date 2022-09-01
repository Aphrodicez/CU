s = []

n = int(input())
for i in range(n):
    s.append(int(input()))

s += [int(x) for x in input().split()]

while True:
    val = int(input())
    if val == -1:
        break
    s.append(val)

ans = []

for i in range(len(s)):
    ans = [s[i]] + ans if i % 2 else ans + [s[i]]

print(ans)