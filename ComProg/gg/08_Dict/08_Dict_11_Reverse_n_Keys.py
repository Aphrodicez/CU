def reverse(d):
    # d เป็น dict ที่มี value ไม่ซ้ำกัน
    # คืน dict ใหม่ที่เก็บ key,value ที่ค่าเป็น value, key ของ d ที่ได้รับ
    return {value : key for key, value in d.items()}
 
def keys(d, v):
    # คืนลิสต์ที่เก็บค่าของ keys ใน d (เรียงยังไงก็ได้) ที่มีค่า value เท่ากับ v
    return [key for key in d.keys() if d[key] == v]

exec(input().strip())