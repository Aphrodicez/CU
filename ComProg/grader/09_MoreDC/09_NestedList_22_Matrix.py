def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append( float(e) )
        m.append(r)
    return m

def mult_c(c, A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][j] *= c


    return A

def mult(A, B):
    if len(A) == 0:
        return None

    if len(B) == 0:
        return A

    rows_1 = len(A)
    cols_1 = len(A[0])
    rows_2 = len(B)
    cols_2 = len(B[0])
    
    ans = [[0 for j in range(cols_2)] for i in range(rows_1)]

    for i in range(rows_1):
        for j in range(cols_2):
            for k in range(cols_1):
                ans[i][j] += A[i][k] * B[k][j]

    return ans

exec(input().strip()) # ต้องมีคำสั่งนี้ตอนส่งให้ Grader ตรวจ