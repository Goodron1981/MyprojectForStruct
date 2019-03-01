import os

from runapp.Finapp.save_result import save_fresh
from runapp.Finapp.take_subtitle import get_path_to_folderbjects
from runapp.Finapp.take_text import parsepage
from runapp.Finapp.take_title import get_title

def loadAll(startyear, finyear, domain, pathtoperiod):
    mymass = []
    loadPath = pathtoperiod + "/forload"
    if not os.path.exists(loadPath):
        os.makedirs(loadPath)
    # print(loadPath)
    print("Скачиваем все страницы периода:", pathtoperiod)

    os.system("/usr/local/bin/wayback_machine_downloader -o '/\.(html|htm)$/i' " + domain + ' -f ' + str(
        startyear) + ' -t ' + str(finyear) + ' -d ' + loadPath)

    print("Закончили скачивать все страницы периода:", pathtoperiod)

    os.system("find " + loadPath + " -name '*.htm*' > " + loadPath + "/loadlist.txt")
    print('find ' + loadPath + ' -name "*.htm" > ' + loadPath + '/loadlist.txt')
    print("loadlist:")
    f = open(loadPath + "/loadlist.txt")
    for line in f.readlines():
        butline = filter_non_printable(line)
        mymass.append(butline)

    for path in mymass:
        fin_format = parsepage(path)
        if len(fin_format) > 1400:
            category = get_path_to_folderbjects(path)
            title = get_title(path)
            save_fresh(title, fin_format, category,path, domain)

def filter_non_printable(str):
  return ''.join([c for c in str if ord(c) > 31 or ord(c) == 9])