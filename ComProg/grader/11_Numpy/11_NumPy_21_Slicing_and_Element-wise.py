from turtle import shape
import numpy as np

def sum_2_rows( M ):
    # คืนผลที่ได้จากการรวมจำนวนในคอลัมน์เดียวกันของแถวที่ติดกันทีละคู่แถว
    # เช่น M = [[ 0, 1, 2, 3], ได้ [[ 4, 6, 8, 10],
    # [ 4, 5, 6, 7], [20, 22, 24, 26]]
    # [ 8, 9, 10, 11],
    # [12, 13, 14, 15]]
    return M[0::2] + M[1::2]

def sum_left_right( M ):
    # คืนผลที่ได้จากการรวมจำนวนของครึ่งซ้ายกับครึ่งขวาของ M
    # เช่น M = [[ 0, 1, 2, 3], ได้ [[ 2, 4],
    # [ 4, 5, 6, 7], [10, 12],
    # [ 8, 9, 10, 11], [18, 20],
    # [12, 13, 14, 15]] [26, 28]]
    return M[:, : M.shape[1] // 2] + M[:, M.shape[1] // 2 :]

def sum_upper_lower( M ):
    # คืนผลที่ได้จากการรวมจำนวนของครึ่งบนกับครึ่งล่างของ M
    # เช่น M = [[ 0, 1, 2, 3], ได้ [[ 8, 10, 12, 14],
    # [ 4, 5, 6, 7], [16, 18, 20, 22]]
    # [ 8, 9, 10, 11], 
    # [12, 13, 14, 15]] 
    return M[ : M.shape[0] // 2, :] + M[M.shape[0] // 2 :, :]

def sum_4_quadrants( M ):
    # คืนผลที่ได้จากการแบ่ง M เป็น 4 จตุภาค และรวมจำนวนที่ตำแหน่งตรงกันในแต่ละจตุภาค
    # เช่น M = [[ 0, 1, 2, 3], ได้ [[20, 24],
    # [ 4, 5, 6, 7], [36, 40]]
    # [ 8, 9, 10, 11], 
    # [12, 13, 14, 15]] 
    return M[ : M.shape[0] // 2, : M.shape[1] // 2] + M[ : M.shape[0] // 2, M.shape[1] // 2 : ] + M[ M.shape[0] // 2: , : M.shape[1] // 2] + M[ M.shape[0] // 2 : , M.shape[1] // 2 : ]

def sum_4_cells( M ):
    # คืนผลที่ได้จากการรวมจำนวนที่ติดกัน 4 ตัว ตามรูปแบบในตัวอย่างข้างล่างนี้
    # เช่น M = [[ 0, 1, 2, 3], ได้ [[10, 18],
    # [ 4, 5, 6, 7], [42, 50]]
    # [ 8, 9, 10, 11], 
    # [12, 13, 14, 15]]
    return M[::2, ::2] + M[::2, 1::2] + M[1::2, ::2] + M[1::2, 1::2]

def count_leap_years( years ):
    # years เป็นอาเรย์เก็บปี พ.ศ.
    # คืนจำนวนปีใน years ที่เป็นปีอทิกสุรทิน (ปีที่ ก.พ. มี 29 วัน)
    years -= 543
    return np.sum(np.logical_or(np.logical_and(years % 4 == 0, years % 100 != 0), years % 400 == 0))

exec(input().strip()) # ต้องมีคำสั่งนี้ ตรงนี้ตอนส่งให้ Grader ตรวจ