courses_filename = input()
teachers_filename = input()
database_filename = input()

courses = open(courses_filename, 'r').read().split()
teachers = open(teachers_filename, 'r').read().split()
database = open(database_filename, 'r').read().split()

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
    if idx_course not in courses_dict or idx_teacher not in teachers_dict:
        print('record error')
    else:
        print(courses_dict[idx_course] + ',' + teachers_dict[idx_teacher])