months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

na, ma, da, ya = input().split()
nb, mb, db, yb = input().split()

da = int(da[:-1])
db = int(db[:-1])
suma = (ya < yb) * 100 + (months.index(ma) < months.index(mb)) * 10 + (da < db)
sumb = (ya > yb) * 100 + (months.index(ma) > months.index(mb)) * 10 + (da > db)

ans = []

if suma >= sumb:
    ans.append(na)
if sumb >= suma:
    ans.append(nb)

print(*ans)