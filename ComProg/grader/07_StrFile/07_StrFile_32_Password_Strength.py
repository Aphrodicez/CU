numseq = '01234567890'
alpseq = 'abcdefghijklmnopqrstuvwxyz'
keypat = [
    '!@#$%^&*()_+',
    'qwertyuiop',
    'asdfghjkl',
    'zxcvbnm',
]

def no_lowercase(t): # return True if no lowercase, otherwise return False
    return not any(x.islower() for x in t)

def no_uppercase(t):
    return not any(x.isupper() for x in t)

def no_number(t):
    return not any(x.isdigit() for x in t)

def no_symbol(t):
    return not any(not(x.isalpha() or x.isdigit()) for x in t)

def character_repetition(t):
    return any(len(set(t[i : i + 4])) == 1 for i in range(len(t) - 3))

def number_sequence(t):
    return any(t[i : i + 4] in numseq or t[i : i + 4][:: -1] in numseq for i in range(len(t) - 3))

def letter_sequence(t):
    return any(t[i : i + 4].lower() in alpseq or t[i : i + 4][:: -1].lower() in alpseq for i in range(len(t) - 3))

def keyboard_pattern(t):
    for s in keypat:
        if any(t[i : i + 4].lower() in s or t[i : i + 4][:: - 1].lower() in s for i in range(len(t) - 3)):
            return True
    return False

#-----------------------------
passw = input().strip()
errors = []

if len(passw) < 8:
    errors.append("Less than 8 characters")

if no_lowercase(passw):
    errors.append("No lowercase letters")

if no_uppercase(passw):
    errors.append("No uppercase letters")

if no_number(passw):
    errors.append("No numbers")

if no_symbol(passw):
    errors.append("No symbols")

if character_repetition(passw):
    errors.append("Character repetition")

if number_sequence(passw):
    errors.append("Number sequence")

if letter_sequence(passw):
    errors.append("Letter sequence")

if keyboard_pattern(passw):
    errors.append("Keyboard pattern")
    
if len(errors) == 0:
    errors.append("OK")

print(*errors, sep = "\n")