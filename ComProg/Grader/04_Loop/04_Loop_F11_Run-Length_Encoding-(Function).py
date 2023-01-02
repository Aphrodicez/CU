def RLE(t):
    ans = []
    last = 0
    cnt = 0
    for i in range(len(t)):
        if t[last] != t[i]:
            ans.append([t[last], cnt])
            cnt = 0
            last = i
        cnt += 1
    if cnt:
        ans.append([t[last], cnt])
    return ans
    
exec(input())