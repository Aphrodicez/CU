import numpy as np

def mult_table(nrows, ncols):
    # คืนอาเรย์ที่มี shape เป็น (nrow, ncols) ภายในเก็บตารางสูตรคูณ (ดูตัวอย่างข้างล่าง)
    return np.reshape(np.arange(1, nrows + 1), (nrows, 1)) * np.arange(1, ncols + 1)

exec(input().strip()) # ต้องมีคำสั่งนี้ ตรงนี้ตอนส่งให้ Grader ตรวจ