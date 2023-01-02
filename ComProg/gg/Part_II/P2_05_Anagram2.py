a = input()
b = input()

print(a)

cnt = 0

for c in range(ord('a'), ord('z') + 1):
    diff = a.lower().count(chr(c)) - b.lower().count(chr(c))
    if diff > 0:
        print(' - remove ' + str(diff) + ' ' + chr(c) + '\'s' * (diff > 1))
        cnt += 1

if cnt == 0:
    print(' - None')

print(b)

cnt = 0

for c in range(ord('a'), ord('z') + 1):
    diff = b.lower().count(chr(c)) - a.lower().count(chr(c))
    if diff > 0:
        print(' - remove ' + str(diff) + ' ' + chr(c) + '\'s' * (diff > 1))
        cnt += 1

if cnt == 0:
    print(' - None')