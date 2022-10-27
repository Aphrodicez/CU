def file2list(filename):
    file = open(filename, 'r')

    file_list = []

    while True:
        line = file.readline().strip()
        if len(line) == 0:
            break
        file_list.append(line)
    
    return file_list

def compare(s, original):
    if len(s) != len(original):
        return False
    
    s = s.lower()
    original = original.lower()
    
    for i in range(len(original)):
        if original[i] == '?':
            continue
        if s[i] != original[i]:
            return False
    
    return True

def solve(s, original, target):
    ans = ''

    s = '/' + s # เพิ่ม slash ไปช่องหน้าสุด เพื่อให้ง่ายต่อการทำ

    l = 0
    r = s.find('/', l + 1)

    while True:
        if r == -1:
            break

        if compare(s[l + 1 : r], original):
            ans += '/' + target
        else:
            ans += '/' + s[l + 1 : r]

        l = r
        r = s.find('/', l + 1) # หา '/' ตั้งแต่ตำแหน่งที่ l + 1 เป็นต้นไป

    ans += '/' + s[l + 1 : ] # string ที่ค้างอยู่หลัง '/' ตัวสุดท้าย

    return ans[1 : ]

# ---------- Main ---------- #

data_filename = input().strip()
original = input().strip()
target = input().strip()

data = file2list(data_filename)

for line in data:
    print(solve(line, original, target))