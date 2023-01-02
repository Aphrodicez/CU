months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

d, m, y = map(int, input().split('/'))

print(months[m], str(d) + ',', y)