import re

def isPhoneNumber(text):
    if len(text) != 9:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,6):
        if not text[i].isdecimal():
            return False
    if text[6] != '-':
        return False
    for i in range(7,9):
        if not text[i].isdecimal():
            return False
    if text[9] != '-':
        return False
    for i in range(8,10):
        if not text[i].isdecimal():
            return False
    return True

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d-\d\d-\d\d)')
mo = phoneNumRegex.search('my number: 857-95-47-36')
print('Phone Number:' + mo.group())
