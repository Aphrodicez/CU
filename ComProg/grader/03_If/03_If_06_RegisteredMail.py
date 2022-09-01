n = int(input())

if n > 2000:
    print('Reject')
    exit()
  
m = [100, 250, 500, 1000, 2000]
g = [18, 22, 28, 38, 58]
ans = min(i for i in range(len(m)) if n <= m[i])

print(g[ans])