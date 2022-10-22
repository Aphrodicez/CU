scores = []

filename, year = [x.strip() for x in input().split()]

with open(filename, 'r') as f:
    while True:
        s = f.readline().strip()
        if len(s) == 0:
            break
        student_id, score = [x.strip() for x in s.split()]
        if student_id[:2] != year[2:]:
            continue
        scores.append(float(score))
    
if len(scores) == 0:
    print('No data')
else:
    print(min(scores), max(scores), sum(scores) / len(scores))