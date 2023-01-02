s = ''.join([x if x.isalpha() or x.isdigit() else ' ' for x in input()]).split()
print(s[0].lower() + ''.join(x.lower().capitalize() for x in s[1 : ]))