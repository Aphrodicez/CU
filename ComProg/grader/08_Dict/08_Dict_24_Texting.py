t2k_dict = {
    'a' : '2', 'b' : '22', 'c' : '222',
    'd' : '3', 'e' : '33', 'f' : '333',
    'g' : '4', 'h' : '44', 'i' : '444',
    'j' : '5', 'k' : '55', 'l' : '555',
    'm' : '6', 'n' : '66', 'o' : '666',
    'p' : '7', 'q' : '77', 'r' : '777', 's' : '7777',
    't' : '8', 'u' : '88', 'v' : '888',
    'w' : '9', 'x' : '99', 'y' : '999', 'z' : '9999',
    ' ' : '0'
}

k2t_dict = {value : key for key, value in t2k_dict.items()}

def text2keys(text):
    keys = []
    for x in text.lower():
        if x in t2k_dict.keys():
            keys += [t2k_dict[x]]
    return ' '.join(keys)

def keys2text(keys):
    text = ''
    for x in keys.split():
        if x in k2t_dict.keys():
            text += k2t_dict[x]
    return text

# ต้องมีคำสั่งนี้ข้างล่างนี้ ตอนส่ง ให้ Grader ตรวจ

exec(input().strip())