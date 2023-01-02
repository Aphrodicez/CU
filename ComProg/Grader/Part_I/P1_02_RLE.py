opr = input()

ans = []

if opr == 'str2RLE':
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
    exit()

if opr == 'RLE2str':
    s = input().split()
    ans = ''
    for i in range(0, len(s), 2):
        ans += s[i] * int(s[i + 1])
    print(ans)
    exit()

print('Error')