a = [x.lower() for x in input() if x.isalpha()]
b = [x.lower() for x in input() if x.isalpha()]
print('YES' if sorted(a) == sorted(b) else 'NO')