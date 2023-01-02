def spiral_square(n):
    # n is a positive odd number
    a = [[0 for j in range(n)] for i in range(n)]
    di = [0, -1, 0, 1]
    dj = [-1, 0, 1, 0]
    
    i, j = n - 1, n - 1
    val = n * n
    k = 0
    
    while val > 1:
        k = k - 1
        while True:
            nexti = i + di[k]
            nextj = j + dj[k]
            k = (k + 1) % 4
            if nexti < 0 or nextj < 0 or nexti > n - 1 or nextj > n - 1:
                continue
            if a[nexti][nextj]:
                continue
            break
        
        a[i][j] = val
        i, j = nexti, nextj
        val -= 1

    a[i][j] = val

    return a
 
def print_square(S):
    # เรียกใช้ฟังก์ชันนี้เพื่อแสดงค่าของ S ที่เป็นลิสต์ของลิสต์ของจำนวนเต็ม
    for i in range(len(S)):
        print(' '.join([(2 * ' ' + str(e))[-3 : ] for e in S[i]]))
    return 

exec(input().strip()) # ต้องมีคำสั่งนี้ ตรงนี้ ตอนส่งให้ Grader ตรวจ 