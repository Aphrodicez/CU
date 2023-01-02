def pattern1(nrows, ncols):
    # nrows >= 0, ncols >= 0
    return [[((ncols * i) + j + 1) for j in range(ncols)] for i in range(nrows)]

def pattern2(nrows, ncols):
    # nrows >= 0, ncols >= 0
    return [[(i + (nrows * j) + 1) for j in range(ncols)] for i in range(nrows)]

def pattern3( N ): # N >= 0
    if N == 0:
        return []
    
    ans = [[0 for j in range(N)] for i in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(i, N):
            cnt += 1
            ans[i][j] = cnt

    return ans

def pattern4( N ): # N >= 0
    if N == 0:
        return []
    
    ans = [[0 for j in range(N)] for i in range(N)]
    cnt = 0

    for j in range(N):
        for i in range(j, -1, -1):
            cnt += 1
            ans[i][j] = cnt

    return ans

def pattern5( N ): # N >= 0
    if N == 0:
        return []
    
    ans = [[0 for j in range(N)] for i in range(N)]
    cnt = 0

    for j in range(N):
        for i in range(N - j):
            cnt += 1
            ans[i][j + i] = cnt

    return ans

def pattern6( N ): # N >= 0
    if N == 0:
        return []
    
    ans = [[0 for j in range(N)] for i in range(N)]
    cnt = 0

    i, j = 0, 0

    while True:
        cnt += 1
        ans[i][j] = cnt
        
        if i == 0 and j == N - 1:
            break

        if (j - i) % 2 == 0:
            if j == N - 1:
                i -= 1
            else:
                i += 1
                j += 1
        elif (j - i) % 2 == 1:
            if i == 0:
                j += 1
            else:
                i -= 1
                j -= 1   

    return ans

exec(input().strip())