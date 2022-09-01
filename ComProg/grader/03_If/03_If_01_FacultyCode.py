faculty = [1, 2] + list(range(20, 40 + 1)) + [51, 53, 55, 58]
faculty = [('0' + str(x))[-2:] for x in faculty]

print('OK' if input() in faculty else 'Error')