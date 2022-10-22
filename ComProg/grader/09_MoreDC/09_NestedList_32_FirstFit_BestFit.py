def first_fit(L, e): # นำ e ใสรายการย่อยใน L ด้วยวิธี first fit
    for x in L:
        if sum(x) + e <= 100:
            x.append(e)
            return 
    L.append([e])

def best_fit(L, e): # นำ e ใส่รายการย่อยใน L ด้วยวิธี best fit
    idx = -1
    mx = -1
    for i, x in enumerate(L):
        if sum(x) + e <= 100:
            if mx < sum(x) + e:
                idx = i
                mx = sum(x) + e
    
    if idx == -1:
        L.append([e])
        return
    L[idx].append(e)

def partition_FF(D): # คืนลิสต์ของลิสต์ที่ได้จากการแบ่งข้อมูลใน D ด้วย first fit
    ans = []
    for x in D:
        first_fit(ans, x)
    return ans

def partition_BF(D): # คืนลิสต์ของลิสต์ที่ได้จากการแบ่งข้อมูลใน D ด้วย best fit
    ans = []
    for x in D:
        best_fit(ans, x)
    return ans

exec(input().strip()) # ต้องมีคำสั่งนี้ ตรงนี้ตอนส่ง ให้ Grader ตรวจ