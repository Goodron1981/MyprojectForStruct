import openpyxl
from runapp.ContinueApp.parsearhiv import loadarhivpage
from runapp.ContinueApp.teke_Periods import getlistperiod
from runapp.ContinueApp.validPeriodList import get_valid_list
from runapp.For_Metriks.all_function_metriks import count_domens
from filelock import FileLock


def validnewdomain(newlist, oldlist):

    for elemdomain in newlist:
        newdomain = elemdomain.lower()
        valid = newdomain in oldlist
        if not valid and newdomain:
            print("Новый домен :", newdomain)
            alllistarhiv = loadarhivpage(newdomain)
            period_list = getlistperiod(alllistarhiv)
            # Далее разбивается по периодам
            get_valid_list(period_list,newdomain)
            latest()
            wb = openpyxl.load_workbook('/home/max/fordomens/OldDomens.xlsx')
            sheet = wb['Лист1']
            last_row = len(sheet['A:A'])
            sheet['A' + str(last_row + 1)].value = newdomain
            wb.save('/home/max/fordomens/OldDomens.xlsx')
            f = open('/home/max/fordomens/Valid.txt', 'a')
            f.write('0')
            f.close()
            count_domens()

def latest():
    while (True):
        f = open('/home/max/fordomens/Valid.txt', 'r+')
        mytest = f.read()
        if len(mytest) > 0:
            test = mytest[-1]
        else:
            test = mytest
        if not test or '0' == test:
            f.write('1')
            f.close()
            print("Запись")
            break
        else:
            f.close()
            print("Заянт")
            continue