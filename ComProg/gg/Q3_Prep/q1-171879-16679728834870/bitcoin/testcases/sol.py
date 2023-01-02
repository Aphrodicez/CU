weeks = int(input())

fast_ema = []
slow_ema = []

p = [0.00]

for i in range(weeks):
    p += list(map(float, input().strip().split(',')))

qs = [0.00]
ch = False

for d in range(1, 7 * weeks + 1):
    qs.append(qs[d - 1] + p[d])
    if d >= 7:
        a = 2.00 / (1 + 7)
        if d == 7:
            val = (1.00 / 7) * qs[d]
        else:
            val = a * p[d] + fast_ema[-1] * (1 - a)
        fast_ema.append(val)

    if d >= 14:
        a = 2.00 / (1 + 14)
        if d == 14:
            val = (1.00 / 14) * qs[d]
        else:
            val = a * p[d] + slow_ema[-1] * (1 - a)
        slow_ema.append(val)

    if d > 14:
        #print(fast_ema[-1], slow_ema[-1])
        if fast_ema[-1] > slow_ema[-1] and fast_ema[-2] <= slow_ema[-2]:
            ch = True
            print('BUY at', '%.2f' % (p[d]))
        if fast_ema[-1] < slow_ema[-1] and fast_ema[-2] >= slow_ema[-2]:
            ch = True
            print('SELL at', '%.2f' % (p[d]))

if not ch:
    print('No results')