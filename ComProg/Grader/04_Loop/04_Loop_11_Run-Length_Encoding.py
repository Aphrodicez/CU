ans = []

s = input()

last = 0
cnt = 0

for i in range(len(s)):
    if s[i] != s[last]:
        ans += [s[last], str(cnt)] 
        cnt = 0
    cnt += 1
    last = i

ans += [s[last], str(cnt)]

print(' '.join(ans))