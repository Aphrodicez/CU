st = '()[]'
en = '[]()'

ans = ''

for x in input():
    ans += x if x not in st else en[st.index(x)]

print(ans)