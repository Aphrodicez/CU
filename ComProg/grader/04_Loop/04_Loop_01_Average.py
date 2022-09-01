_sum = 0
cnt = 0

while True:
    n = input()
    if n == 'q':
        break
    n = float(n)
    _sum += n
    cnt += 1

print(round(_sum / cnt, 2) if cnt else 'No Data')