import openpyxl


def saveseconds(startyear, finyear, name_domain, countunikal):
    wb = openpyxl.load_workbook('/home/max/websites/second_grade/second_grade.xlsx')
    sheet = wb['second_grade']
    newrow = [name_domain,startyear,finyear,countunikal]
    sheet.append(newrow)
    wb.save('/home/max/websites/second_grade/second_grade.xlsx')
    print("Записано во 2-й сорт : ", name_domain, " ,", startyear, " ,", finyear, " ,", countunikal)
