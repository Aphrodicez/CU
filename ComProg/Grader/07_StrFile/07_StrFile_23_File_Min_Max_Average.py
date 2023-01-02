def file2list(filename):
    file = open(filename, 'r')
    file_list = []

    while True:
        s = file.readline().strip()
        if len(s) == 0:
            break
        file_list.append(s)

    return file_list

scores = []

filename, year = [x.strip() for x in input().split()]

data = file2list(filename)

for line in data:
    student_id, score = [x.strip() for x in line.split()]

    if student_id[: 2] != year[2 : ]:
        continue
    scores.append(float(score))
    
if len(scores) == 0:
    print('No data')
else:
    print(min(scores), max(scores), sum(scores) / len(scores))