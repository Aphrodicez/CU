s = input()

scores = [0] * len(s)

for i in range(len(s)):
    if s[i] == '/':
        scores[i] = 10 - scores[i - 1]
        continue
    scores[i] += 10 if s[i] == 'X' else int(s[i])

ans = [0] * 21
cnt = 2
st = 0

for i in range(len(s)):
    ans[cnt // 2] += scores[i]
    if s[i] == 'X':
        ans[cnt // 2] += scores[i + 2] if i + 2 <= len(s) - 1 else 0
    if s[i] in 'X/':
        ans[cnt // 2] += scores[i + 1] if i + 1 <= len(s) - 1 else 0
    cnt += 1
    if s[i] == 'X':
        cnt += 1
    if cnt // 2 == 10:
        st = i + 1
        break
    
ans[10] = sum(scores[st:])
ans = ans[:11]

q = int(input())

print(ans[q] if q >= 1 and q <= 10 else sum(ans))