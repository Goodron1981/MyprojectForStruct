import os
import datetime

import openpyxl

from runapp.Finapp.make_paragraph import maker_par_ph
from runapp.For_Metriks.all_function_metriks import count_articles


def save_fresh(title, content, category, originpath, savedomain):
    domain_dir = "/home/max/websites/fresh_content/all_subjects/" + category + "/" + savedomain
    if not os.path.exists(domain_dir):
        os.makedirs(domain_dir)

    # 1 узнать послединий использованый номер
    wb = openpyxl.load_workbook('/home/max/websites/fresh_content/listfiles.xlsx')
    sheet = wb['ListTXT']
    last_row = len(sheet['A:A'])
    if last_row > 1:
        last_file = sheet['A' + str(last_row)].value
        print(last_file)
        fil_name = last_file.split('.')[0]
        last_num = int(fil_name)
    else:
        last_num = 0
    new_num = last_num + 1
    new_file = "{0:06}".format(new_num) + ".txt"
    pathfile = domain_dir + '/' + new_file
    nowtime = datetime.datetime.now()
    formattime = nowtime.strftime('%d.%m.%Y %H:%M:%S')
    sheet['B' + str(last_row + 1)] = formattime
    sheet['A' + str(last_row + 1)] = new_file
    sheet['C' + str(last_row + 1)] = pathfile
    sheet['D' + str(last_row + 1)] = originpath
    # sheet['B' + str(last_row + 1)].number_format = 'dd.mm.yyyy h:mm:ss'
    wb.save('/home/max/websites/fresh_content/listfiles.xlsx')
    print("Записано во 1-й сорт : ", new_file, " ,", formattime)
    withparcont = maker_par_ph(content)

    alltext = "<category>" + category + "</category>" + "\n"
    alltext2 = alltext + "<title>" + title + "</title>" + "\n"
    alltext3 = alltext2 + "<article>" + withparcont + "</article>"
    my_file2 = open(domain_dir + '/' + new_file, 'w')
    my_file2.write(alltext3)
    my_file2.close()
    count_articles()
    # 3 записать данные в файл данные в формате xml но с расширением txt
