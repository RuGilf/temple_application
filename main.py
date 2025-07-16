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
Label(root, text = '☦ Во имя Отца, и Сына, и Святого Духа. Аминь. ☦', font='Helvetica 9 bold').grid(column=0, row=3)
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
Label(root, text = '☦ Слава Отцу, и Сыну, и Святому Духу, ныне и присно, и во веки веков. Аминь. ☦', font='Helvetica 9 bold').grid(column=0, row=18)

root.mainloop()