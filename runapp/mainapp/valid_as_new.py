import openpyxl
from runapp.ContinueApp.parsearhiv import loadarhivpage
from runapp.ContinueApp.teke_Periods import getlistperiod
from runapp.ContinueApp.validPeriodList import get_valid_list
from runapp.For_Metriks.all_function_metriks import count_domens


def validnewdomain(newlist, oldlist):
    wb = openpyxl.load_workbook('/home/max/fordomens/OldDomens.xlsx')
    # workbook = xlrd.open_workbook('/home/max/fordomens/OldDomens.xlsx')
    sheet = wb['Лист1']
    oldcount = len(oldlist)
    for elemdomain in newlist:
        newdomain = elemdomain.lower()
        valid = newdomain in oldlist
        if not valid and newdomain:
            print("Новый домен :", newdomain)
            alllistarhiv = loadarhivpage(newdomain)
            period_list = getlistperiod(alllistarhiv)
            # Далее разбивается по периодам
            get_valid_list(period_list,newdomain)

            oldcount = oldcount + 1
            sheet['A' + str(oldcount)].value = newdomain
            wb.save('/home/max/fordomens/OldDomens.xlsx')
            count_domens()
