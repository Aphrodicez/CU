C = ['AEILNORSTU', 'DG', 'BCMP', 'FHVWY', 'K', 'JX', 'QZ']
P = [1, 2, 3, 4, 5, 8, 10]

def letter_point(c):
    # คืนคะแนนของตัวอักษรในตัวแปร c ตามตารางที่ให้ไว้
    return [P[i] for i,v in enumerate(C) if c in v][0]

def word_point(w):
    # คืนคะแนนของคำที่เก็บในตัวแปร w ที่หาได้จากผลรวมของคะแนนของทุกตัวอักษรใน w
    return sum(letter_point(x) for x in w)

words = input().split()
for p, w in sorted([(-word_point(w), w) for w in words]):print(w, -p)