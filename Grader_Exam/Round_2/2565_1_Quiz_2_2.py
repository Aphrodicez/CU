def match(word, pattern, include_chars, exclude_chars):
    if len(word) != len(pattern):
        return False
    q = ''
    for i in range(len(word)):
        if pattern[i] == '?':q += word[i]
        elif word[i] != pattern[i]: return False
    if any([x for x in exclude_chars if x in q]):return False
    for x in include_chars:
        if q.count(x) < include_chars.count(x):return False
    return True

exec(input()) # DON'T remove this line