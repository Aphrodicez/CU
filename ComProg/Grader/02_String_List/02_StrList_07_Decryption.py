s = ' ' + input()

val = 10000 + int(''.join(s[i] for i in range(4, 32 + 1, 7))) + int(''.join(s[i] for i in range(8, 28 + 1, 5)))
val = str(val)[-4:-1]

ans = val + chr(65 + int(str(sum(int(x) for x in val))[-1]))
print(ans)