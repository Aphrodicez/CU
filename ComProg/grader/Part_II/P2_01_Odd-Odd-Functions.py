def is_odd(n):
    # คืน (True/False) ว่า n เป็นจำนวนคี่หรือไม่
    return (n % 2 == 1)
 
def has_odds(x):
    # คืน (True/False) ว่า x เป็นลิสต์ที่มีข้อมูลบางตัวเป็นจำนวนคี่
    return any(is_odd(i) for i in x)

def all_odds(x):
    # คืน (True/False) ว่า x เป็นลิสต์ที่มีข้อมูลทุกตัวเป็นจำนวนคี่
    return not any(not is_odd(i) for i in x)
 
def no_odds(x):
    # คืน (True/False) ว่า x เป็นลิสต์ที่มีไม่มีข้อมูลที่เป็นจำนวนคี่เลย
    return not has_odds(x)

def get_odds(x):
    # คืนลิสต์ที่มีจำนวนคี่ที่มีเก็บในลิสต์ x (ลำดับก่อนหลังให้เป็นไปตามลำดับเดียวกับใน x)
    # เช่น x = [1,2,3,5,0] จะได ้ผลคือ [1,3,5]
    return [i for i in x if is_odd(i)]

def zip_odds(a, b):
    # คืนลิสต์ที่สร้างจากการนำจำนวนคี่ใน a และ b มาสลับกันเก็บในลิสต์ผลลัพธ์ (เริ่มจากใน a ก่อน)
    # เช่น a = [0,8,1,2,4,6,5,7,9,2,3] กับ b = [4,19,11,12,10,17] จะได้ คือ
    # [1,19,5,11,7,17,9,3]
    a_odds = get_odds(a)
    b_odds = get_odds(b)
    
    ans = []
    i, j = 0, 0

    while i < len(a) or j < len(b):
        ans += a_odds[i : i + 1]
        ans += b_odds[j : j + 1]
        i += 1
        j += 1
    
    return ans
 
exec(input().strip()) # ต้องมีคำสั่งนี้ ตรงนี้ ตอนส่งให้ Grader ตรวจ