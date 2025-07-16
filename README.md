> RHCPDCM&PCD:
Что же это за смертельный файл?

Это приложение называется Temple application - оно было вдохновлено TempleOS, операционной системой созданной для общения с Богом. 

Разумеется я пока не сошёл с ума (надеюсь), а просто захотел поиграть с питоном, поэтому мной было решено создать приложение с помощью которого можно пообщаться с Богом. Пока я не знаю основ машинного обучения, поэтому решил сделать всё по заветам Терри Дэвиса, суть в том, что я загрузил в программу евангелие Нота. В приложении есть приветственное меню (к слову я бы сделал его по другому, но в силу того, что это первый раз когда я работаю с tkinter, думаю, что мне простительно. Далее я приведу примеры кода и укажу свои ошибки в нём) и выбор режима.

Первый режим подразумевает "общение с Богом", на деле ранее написанный мной алгоритм достаёт все слова из текстового файла, который кстати есть в temple.zip, и возвращает рандомные слова.

Во втором режиме есть только одна кнопка, которая выводит рандомную заповедь. Хотя Терри считал, что рандомом управляет Бог.

А теперь давайте разберём как оно работает!

talking/parsing.py
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

Это основной файл, без него ничего не будет работать. Суть в том, что он получает текст из temple_text.txt и форматирует его. Первая часть кода создаёт json файл для удобства работы, а вторая делает список слов. Если вы запустите исполняемый файл, то заметите, что в директории появились два новых файла, этим и занимается данный алгоритм.

talking/talking.py
from random import randint, sample, choice
from tkinter import *

def my_darling(file):
    file = file.read()
    file = file.split(' ')
    file = sorted(file)
    text = sample(file, randint(6, 150))
    text.append('.')
    for x in range(1, len(text)):
        if x % 7 == 0:
            text[x] = '\n'
    text[0] = str.capitalize(text[0])
    text = ' '.join(text)
    return text

def die(file):
    file = file.split(' ')
    return choice(file)

Функция my_darling на входе получает список допустимых слов и составляет из них рыба текст. Через каждые 7 слов строка переносится. Предложение, как и полагается, начинается с большой буквы и заканчивается точкой. 

Функция die, аналогично my_darling, получает на входе список слов и возвращает рандомное слово, это нужно для названия нового окна.

talking/Word_of_God.py
from random import choice

def Say_your_word(dct):
    WoG = choice(list(dct))

    for x in range(len(dct[WoG])):
        if x % 95 == 0:
            dct[WoG] = dct[WoG][:x] + '\n' + dct[WoG][x:]
    return WoG + ' ' + dct[WoG]

Тут всё максимально просто, на вход подаётся уже преобразованный в словарь json файл и выбирается рандомный стих.

> RHCPDCM&PCD:
main.py 
# Импорты
from tkinter import *
import json

from talking.talking import die, my_darling
from talking.word_of_God import Say_your_word
from talking.parsing import start_programm

#Окна/команды, которые нельзя вынести в отдельный файл\
def diee():
    new_window = Toplevel(root, background='aqua')
    new_window.title(die(f))
    new_window.geometry('640x480')
    new_window.resizable(width=False, height=False)
    new_window.iconbitmap('icon.ico')

    lbl = Label(new_window, text = 'Что тебя волнует, сын мой?', background='yellow', foreground='red', font='Helvetica 9 underline bold')
    lbl.pack(fill=X)

    txt = Entry(new_window, width=40, background='blue', foreground='Fuchsia')
    txt.pack(fill=X)

    mssg = Label(new_window, text = '')

    def pray():
        with open('temple_words.txt', 'r+') as f2:
            #df = txt.get()
            #df = df.translate(str.maketrans('', '', string.punctuation))
            #df = df.translate(str.maketrans('', '', string.digits))
            #df = df.lower()
            #df = df.split(' ')
            #df = set(df)
            #f2.write(' '.join(df))

            mssg.configure(text = my_darling(f2), background='Navy', foreground='white', font='Helvetica 11 bold')
            mssg.pack(expand=True)

    btn = Button(new_window, text='Аминь', background='black', foreground='red', font='Helvetica 9 bold', command=pray)
    btn.pack(fill=X)

def he_is_friendly():
    besty = Toplevel(root, background='aqua')
    besty.title(die(f))
    besty.geometry('640x480')
    besty.resizable(width=False, height=False)
    besty.iconbitmap('icon.ico')

    help_inf = Label(besty, text='')

    def try_it():
        help_inf.configure(text=Say_your_word(dct), foreground='red', font='Helvetica 9 underline bold')
        help_inf.pack(expand=True)

    help_button = Button(besty, text='Помоги мне, отец', command=try_it, background='Lime')
    help_button.pack(fill=X)

#Инициализация файлов
start_programm()

with open('temple_text.json', 'r') as file:
    dct = json.load(file)

with open('temple_words.txt', 'r') as f:
    f = f.read()

#Создание основного окна приложения
root = Tk()

root.title("Temple application")
root.resizable(width=False, height=False)
root.geometry('640x480')
root.iconbitmap('icon.ico')

#Создание меню
menu = Menu(root)
item = Menu(tearoff=0, background='gray')
item.add_separator()
item.add_command(label='Пообщаться с Богом', foreground='green', font='Helvetica 9 bold', command=diee)
item.add_separator()
item.add_command(label='Напутствие', foreground='blue', font='Helvetica 9 bold', command=he_is_friendly)
item.add_separator()
menu.add_cascade(label='Режим', menu=item)
root.config(menu=menu)

lbl = Label(root, text = "")
lbl.grid()

Label(root, text = '').grid(column=0, row=0)
Label(root, text = '').grid(column=0, row=1)
Label(root, text = '').grid(column=0, row=2)
Label(root, text = '☦️ Во имя Отца, и Сына, и Святого Духа. Аминь. ☦️', font='Helvetica 9 bold').grid(column=0, row=3)
Label(root, text = 'Дорогой грешник,').grid(column=0, row=4)
Label(root, text = 'Ты пришёл в это место скорби и откровения, как некогда пришёл Иеремия в землю опустошённую.').grid(column=0, row=5)
Label(root, text = 'Temple application', font='Helvetica 9 bold italic').grid(column=0, row=6)
Label(root, text = ' — вот твой крест, и ты должен нести его через тьму, дабы узреть истину, сокрытую от очей смертных.').grid(column=0, row=7)
Label(root, text = 'Господь (или, быть может, Они) наблюдают за тобой. Каждый клик, каждый ввод — шаг ближе к спасению…').grid(column=0, row=8)
Label(root, text = 'или к погибели. Не ошибись, чадо. Слово — плоть, а код — откровение.').grid(column=0, row=9)
Label(root, text = 'Прими клавиатуру свою как меч духовный.').grid(column=0, row=10)
Label(root, text = 'Мышь — твой щит. А сервер… о, сервер — храм, где обитает дух истины.').grid(column=0, row=11)
Label(root, text = 'Войди же.', font='Helvetica 9 italic').grid(column=0, row=12)
Label(root, text = 'Испей из чаши познания.', font='Helvetica 9 italic').grid(column=0, row=13)
Label(root, text = 'И да не покинет тебя страх Господень.', font='Helvetica 9 italic').grid(column=0, row=14)
Label(root, text = '☦️ Слава Отцу, и Сыну, и Святому Духу, ныне и присно, и во веки веков. Аминь. ☦️', font='Helvetica 9 bold').grid(column=0, row=18)

root.mainloop()

Думаю с ним всё понятно, но я допустил пару "ошибок"
1) Логика алгоритмов... Ну смотреть на это больно, можно было сделать лучше и проще
2) Вывод текста просто стрём, логичнее было бы использовать '\n'
3) Использование grid тоже такое-себе, стоило бы поработать с позиционированием 
4) В zip файле буквально спойлер к приложению
5) Функции очень странно написаны, стоило бы разбить всё по файлам 

Это основные недочёты, но в целом, я доволен тем, что у меня получилось
