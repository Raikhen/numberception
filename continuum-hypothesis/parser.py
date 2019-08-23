from pprint import pprint

'''
name: String
age: Number
bt_char: Char
st_char: Char
responses: { speed: Time, num: Number, selected: Char }
'''

f = open('data.txt', 'r')

all = f.read()
subjects = []
temp = all.split('\n\n')[:-1]
subjects_str = [player.split('\n') for player in temp]

for subject in subjects_str:
    # Subject object
    obj = {}

    # Name and age
    obj['name'], obj['age'] = subject[0].rsplit(' ', 1)

    # Chars
    temp = subject[1].split('"')
    obj['bt_char'] = temp[1]
    obj['st_char'] = temp[3]

    # Responses
    subject = subject[2:]
    obj['responses'] = []

    for resp in subject:
        r = {}
        temp = resp.split(' ')
        r['speed'] = temp[-1]
        r['number'] = int(temp[0])
        r['selected'] = temp[1]
        obj['responses'].append(r)

    subjects.append(obj)

pprint(len(subjects))

f.close()
