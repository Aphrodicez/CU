s = input()
x, y = map(int, s.split())

minl, minr = x, y
maxl, maxr = x, y

i = 1
while(True):
    s = input()
    if s == 'Zig-Zag' or s == 'Zag-Zig':
        break
    x, y = map(int, s.split())
    if i % 2:
        x, y = y, x
    minl, minr = min(minl, x), min(minr, y)
    maxl, maxr = max(maxl, x), max(maxr, y)
    i += 1
  
if s == 'Zig-Zag':
    print(minl, maxr)
else:
    print(minr, maxl)