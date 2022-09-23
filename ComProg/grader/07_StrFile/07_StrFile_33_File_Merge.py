def compare(id1, id2):
    if id1[-2 : ] != id2[-2 : ]:
        return id1[-2 : ] < id2[-2 : ]
    return id1 < id2

filename1, filename2 = [x.strip() for x in input().split()]

with open(filename1, 'r') as file1, open(filename2, 'r') as file2:
    stu1 = file1.readline().strip().split()
    stu2 = file2.readline().strip().split()
    while True:
        if len(stu1) == 0 or len(stu2) == 0:
            break
        if compare(stu1[0], stu2[0]):
            print(*stu1)
            stu1 = file1.readline().strip().split()
        else:
            print(*stu2)
            stu2 = file2.readline().strip().split()
    
    while True:
        if len(stu1) == 0:
            break
        print(*stu1)
        stu1 = file1.readline().strip().split()
    
    while True:
        if len(stu2) == 0:
            break
        print(*stu2)
        stu2 = file2.readline().strip().split()