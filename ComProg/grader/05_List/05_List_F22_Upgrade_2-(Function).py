graderank = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']

def index_of(grades, ID):
	for i in range(len(grades)):
		if grades[i][0] == ID:
			return i
	return -1

def upgrade(grades, IDs):
	for ID in IDs:
		for i in range(len(grades)):
			if ID == grades[i][0]:
				grades[i][1] = grades[i][1] if grades[i][1] == 'A' else graderank[graderank.index(grades[i][1]) + 1]
	grades.sort(key = lambda x : x[0])

exec(input())
exec(input())
exec(input())