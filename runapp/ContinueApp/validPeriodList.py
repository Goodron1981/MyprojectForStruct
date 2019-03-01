import os

from runapp.ContinueApp.validAnyPeriod import isunikalPeriod
from runapp.Finapp.loadAllPagePeriod import loadAll
from runapp.Finapp.forsaveseconds import saveseconds


def get_valid_list(list_periods, name_domain):
    # validated_list = []
    countlist = len(list_periods) / 2
    c = 0
    while c < countlist:
        domain_dir = "/home/max/websites/processing_domain/" + name_domain + "/period" + str(c+1)
        if not os.path.exists(domain_dir):
            os.makedirs(domain_dir)
        fromyear = list_periods[2 * c]
        toyear = list_periods[(2 * c) + 1]
        isvalidlist = isunikalPeriod(fromyear, toyear, name_domain, domain_dir)
        boleanValid = isvalidlist.count(True)
        # если в периоде 3 уникальных точки - качаем все
        if boleanValid == 3:
            print("Уникальный период :", domain_dir)
            loadAll(fromyear, toyear, name_domain, domain_dir)
        elif boleanValid > 0:
            saveseconds(fromyear, toyear, name_domain, boleanValid)
        else:
            print("Неуникальный период :", domain_dir)
        c = c + 1
    else:
        print("Неуникальный домен :", name_domain)
    print("Процесс get_valid_list по ", name_domain, " завершен")