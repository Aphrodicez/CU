word = input()
s = input()

for x in '.()\'\"':
    s = s.replace(x, ' ')

print(sum(word == str(x) for x in s.split()))