import json
import string

def start_programm():
    s = 0
    p = 1
    dct = {}

    with open("Temple_text.txt", "r") as file:
        for line in file:
            if line[1] == '.':
                if int(line[0]) > s:
                    s = int(line[0])
                    dct[str(p) + ':' + str(s)] = line[3:]
                else:
                    s = 0
                    p += 1
            else:
                if int(str(line[0]) + str(line[1])) > s:
                    s = int(str(line[0] + str(line[1])))
                    dct[str(p) + ':' + str(s)] = line[3:]
                else:
                    s = 0
                    p += 1

    with open('temple_text.json', 'w', encoding='utf-8') as file:
        json.dump(dct, file, ensure_ascii=False, indent=0)

    with open("Temple_text.txt", "r") as file:
        arr = file.read()
    arr = arr.translate(str.maketrans('', '', string.punctuation))
    arr = arr.translate(str.maketrans('', '', string.digits))
    arr = arr.lower()
    arr = arr.replace('\n', '')
    arr = arr.replace('—', '')
    arr = arr.split(' ')
    arr = set(arr)
    arr = ' '.join(arr)
    with open('temple_words.txt', 'w', encoding='utf-8') as file:
        file.write(arr)