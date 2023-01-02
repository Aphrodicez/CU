prices = {}
sales = {}

n = int(input())

for i in range(n):
    name, price = input().split()
    price = float(price)
    prices[name] = price
    sales[name] = 0

m = int(input())

for i in range(m):
    name, amount = input().split()
    amount = float(amount)
    if name not in prices:
        continue
    sales[name] += prices[name] * amount

mx = max(sales.values())
ans = sorted([name for name in sales.keys() if sales[name] == mx])

if mx == 0:
    print('No ice cream sales')
else:
    print('Total ice cream sales:', sum(sales.values()))
    print('Top sales: ' + ', '.join(ans))