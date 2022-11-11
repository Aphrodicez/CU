# Clockwise
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

r, c = map(int, input().split())

visited = [[False for j in range(c + 10)] for i in range(r + 10)]
a = []

ans = []

def recursive(i, j, state):
    if state == len(word):
        print(ans)
        exit(0)
    for k in range(4):
        nexti = i + di[k]
        nextj = j + dj[k]
        if nexti < 0 or nextj < 0 or nexti > r - 1 or nextj > c - 1: # Check Border
            continue
        if a[nexti][nextj] != word[state]:
            continue
        if visited[nexti][nextj]: # Check Visited
            continue
        visited[nexti][nextj] = True
        ans.append((nexti, nextj))
        recursive(nexti, nextj, state + 1)
        ans.pop()
        visited[nexti][nextj] = False

for i in range(r):
    s = input().strip()
    a.append(s)

word = input().strip()

for i in range(r):
    for j in range(c):
        if a[i][j] == word[0]:
            visited[i][j] = True
            ans.append((i, j))
            recursive(i, j, 1)
            ans.pop()
            visited[i][j] = False