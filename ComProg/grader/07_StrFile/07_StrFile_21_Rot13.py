while True:
    s = input()
    if s == 'end':
        break
    ans = ''
    for x in s:
        if x.isalpha():
            a = 65 if ord(x) - 97 < 0 else 97
            x = chr(((ord(x) - a + 13) % 26) + a)
        ans += x
    print(ans)