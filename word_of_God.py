from random import choice

def Say_your_word(dct):
    WoG = choice(list(dct))

    for x in range(len(dct[WoG])):
        if x % 95 == 0:
            dct[WoG] = dct[WoG][:x] + '\n' + dct[WoG][x:]
    return WoG + ' ' + dct[WoG]