import os

from runapp.ContinueApp.validAnyPeriod import isunikalPeriod


def get_valid_list(list_periods, name_domain):
    validated_list = []
    countlist = len(list_periods) / 2
    c = 0
    while c < countlist:
        domain_dir = name_domain.replace("http://", "/home/max/websites/Processing_Domain/") + "/Period" + str(c+1)
        if not os.path.exists(domain_dir):
            os.makedirs(domain_dir)
        fromyear = list_periods[2 * c]
        toyear = list_periods[(2 * c) + 1]
        isvalidlist = isunikalPeriod(fromyear, toyear, name_domain, domain_dir)
        boleanValid = isvalidlist.count(True)
        # если в периоде 3 уникальных точки - качаем все
        if boleanValid == 3:
            print("Уникальный период :", domain_dir)
            # todo loadAll()
        elif boleanValid > 1:
        # todo savetothirth()
            print("2-сорт :", domain_dir)
        else:
            print("Неуникальный период :", domain_dir)
            # test = [fromyear, toyear]
            # validated_list.append(test)
        c = c + 1
    return validated_list