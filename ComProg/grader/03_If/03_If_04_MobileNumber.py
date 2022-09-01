s = input()
print('Mobile number' if (len(s) == 10 and (s[:2] == '06' or s[:2] == '08' or s[:2] == '09')) else 'Not a mobile number')