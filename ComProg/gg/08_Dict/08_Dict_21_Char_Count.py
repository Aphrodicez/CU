cnt = {}

s = input().lower()

for x in s:
    if not x.isalpha():
        continue
    if x in cnt:
        cnt[x] += 1
    else:
        cnt[x] = 1

ans = sorted(cnt.items(), key = lambda x: (-x[1], x[0]))

for x in ans:
    print(x[0], '->', x[1])