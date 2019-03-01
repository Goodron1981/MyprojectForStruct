import re

from bs4 import BeautifulSoup
from runapp.models import Excludespage


def formathtmltotxt(content):
    trace = BeautifulSoup(content, "html5lib")
    test = trace.find_all('body')
    if len(test)>0:
        bots = trace.find_all('body')[0]
        bebots = bots.get_text()
    else:
        bebots = ""
    # trace = BeautifulSoup(page.data, "html5lib")
    # bots = trace.find_all('body')[0]
    # bebots = bots.get_text()
    bush = bebots.lower()
    exwordlist = Excludespage.objects.all()
    for exword in exwordlist:
        serchword = '\\b' + exword.ex_page + '\\b'
        exvalid = re.search(serchword, bush)
        if exvalid:
            print(exvalid)
            print('Тут')
            bebots = bush = "Bad text."
            break
    print(bush)
    # Обрезка до возможных комментариев
    startserch = bush.find('комментар')
    bebots = bebots[:startserch]

    # удаляем названия с большой буквы на кирилице в фигурных кавычках
    bebots = re.sub("\s*«[А-ЯЁ].*»\s*", " НАЗВАНИЕ КОМПАНИИ ", bebots)
    # удаляем названия с большой буквы на кирилице в обычных кавычках
    bebots = re.sub('\s*"[А-ЯЁ].*"\s*', ' НАЗВАНИЕ КОМПАНИИ ', bebots)

    pattern = re.compile(r'[А-Я].+[!.?]')
    pattern2 = re.compile(r'\s{2}')
    cholks = pattern2.split(bebots)
    mytext = ""
    for cholk in cholks:
        sloer = pattern.findall(cholk)
        for mark in sloer:
            for wen in mark:
                if wen != '\u2192' and wen != '\xd7':
                    mytext = mytext + wen
            mytext = mytext + ' '
        mytext = mytext + ' \n'
    mytext = mytext.replace(".", ". ")
    mytext = re.sub(" \d+\.", "", mytext)
    # исправляем склеивание предложений в переносах
    pattern3 = re.compile(r'[а-яё)][А-ЯЁ«]')
    boki = pattern3.findall(mytext)
    for bet in boki:
        wix = bet[:1] + ". " + bet[1:]
        mytext = mytext.replace(bet, wix)
    # исправляем попадание неверных знаков
    pattern4 = re.compile(r'[\w][^\s\w][\w]')
    boki = pattern4.findall(mytext)
    for bet in boki:
        wix = bet[:2] + " " + bet[2:]
        mytext = mytext.replace(bet, wix)

    validtext = re.split(r'[.!?]', mytext)
    pattern5 = re.compile(r'[а-яё]+')
    group = ""
    for peace in validtext:
        testvalid = pattern5.findall(peace)
        if len(testvalid) > 4:
            group = group + peace + '.'
        pattern6 = re.compile(r'\s{2,}')
        result = pattern6.sub(' ', group)
    return result