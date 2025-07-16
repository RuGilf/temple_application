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
