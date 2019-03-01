# from runapp.ContinueApp.takeownerlist import getownerlist


def getlistperiod(jsonlist):
    # test = len(jsonlist)
    result_list = my_list = []
    for actualpage in jsonlist:
        year = str(actualpage["timestamp"])[:4]
        if not int(year) in my_list:
            my_list.append(int(year))
    my_list.sort()
    print(my_list)
    # my_list = [2004, 2007, 2008, 2009, 2011, 2012, 2015]
    if len(my_list) > 1:
        startyear = my_list[0]
        finyear = my_list[-1]
        result_list = [startyear]
        lenlist = len(my_list)
        print("lenlist : ", lenlist)
        i = 1
        while i < lenlist:
            print("i : ", i)
            valid = my_list[i] - my_list[i - 1]
            if valid > 1:
                result_list.append(my_list[i - 1])
                result_list.append(my_list[i])
            print(result_list)
            i = i + 1
        result_list.append(finyear)
        print(result_list)
    elif len(my_list) > 0:
        result_list = [my_list[0], my_list[0]]
    else:
        result_list = []

        # getownerlist(actualpage, name_domain)
    return result_list
