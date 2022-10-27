n = int(input())

for i in range(n):
    s = input()

    cnt = 0
    for j in s:
        if j != '.':
            break
        cnt += 1
    
    print(('.' * (cnt // 2)) + s[cnt : ])