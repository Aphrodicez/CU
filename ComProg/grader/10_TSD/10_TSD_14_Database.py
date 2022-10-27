def file2list(filename):
    file = open(filename, 'r')
    file_list = []

    while True:
        s = file.readline().strip()
        if len(s) == 0:
            break
        file_list.append(s)

    return file_list

courses_filename = input().strip()
teachers_filename = input().strip()
database_filename = input().strip()

courses = file2list(courses_filename)
teachers = file2list(teachers_filename)
database = file2list(database_filename)

courses_dict = dict()
teachers_dict = dict()
database_dict = dict()

for x in courses:
    idx, course = x.split(',')
    courses_dict[idx] = course

for x in teachers:
    idx, teacher = x.split(',')
    teachers_dict[idx] = teacher

for x in database:
    idx_course, idx_teacher = x.split(',')
    if (idx_course not in courses_dict) or (idx_teacher not in teachers_dict):
        print('record error')
    else:
        print(courses_dict[idx_course] + ',' + teachers_dict[idx_teacher])