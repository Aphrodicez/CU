graderank = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']

ids = []
grades = []

while True:
    s = input()
    if s == 'q':
        break
    id, grade = s.split()
    ids.append(id)
    grades.append(grade)

for x in input().split():
    idx = ids.index(x)
    grades[idx] = grades[idx] if grades[idx] == 'A' else graderank[graderank.index(grades[idx]) + 1]

for i in range(len(ids)):
    print(ids[i], grades[i])