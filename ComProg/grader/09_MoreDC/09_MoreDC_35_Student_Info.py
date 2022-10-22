n = int(input())
student_list = [input() for i in range(n)]
query = set(input().split())

ans = [x for x in student_list if len(set.intersection(query, set(x.split()[1:]))) == len(query)]

ans.sort(key = lambda x : x.split()[0])

if len(ans) == 0:
    print('Not Found')
print(*ans, sep = '\n')