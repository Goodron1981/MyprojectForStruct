import codecs
import os
import json
from runapp.ContinueApp.parse_validate_content import getparse, getcodname
from runapp.ContinueApp.parse_validate_content import isunikal_text


def isunikalPeriod(firstyear, lastyear, Domain, pathDomain):
    # DomainDir = Domain.replace("http://", "/home/max/websites/processing_domain/")
    # directory = os.path.dirname(DomainDir)
    if not os.path.exists(pathDomain):
        os.makedirs(pathDomain)
    validPath = pathDomain + "/forvalid"
    if not os.path.exists(validPath):
        os.makedirs(validPath)

    print('Процесс: isunikalPeriod')
    foop = os.system('/usr/local/bin/wayback_machine_downloader -l -o "/\.(html|htm)$/i" ' + Domain + ' -f ' + str(
        firstyear) + ' -t ' + str(lastyear) + '> "' + pathDomain + '/listimstamps.txt"')
    if foop > 0:
        Domain = "https://" + Domain
        foop = os.system('/usr/local/bin/wayback_machine_downloader -l -o "/\.(html|htm)$/i" ' + Domain + ' -f ' + str(
            firstyear) + ' -t ' + str(lastyear) + '> "' + pathDomain + '/listimstamps.txt"')
        print("2 попытка ",foop)
    print("Загружено с ", firstyear, " по ", lastyear)
    #my_file = open(pathDomain + '/listimstamps.txt', 'r')
    #my_string = my_file.read()
    file_path = pathDomain + '/listimstamps.txt'
    # my_file = open(DomainDir + '/listimstamps.txt', 'r')

    codectext = getcodname(file_path)
    print(codectext)
    with codecs.open(file_path, encoding=codectext, errors='replace') as my_file:
        # my_file = open(file_path, 'r')
        try:
            my_string = my_file.read()
        except UnicodeDecodeError as error:
            my_string = "[]"
            print("Ошибка при чтении файла :", file_path)
        my_file.close()


    print(len(my_string))
    stratarr = my_string.rfind("]")
    finarr = my_string.rfind("[", 0, stratarr)
    result = my_string[finarr + 1:stratarr + 1]
    testarr = result.find("{")
    if testarr > 0:
        finuarr = result.rfind("}") + 1
        my_arr = result[testarr:finuarr]
        myresult = "[" + my_arr + "]"
    else:
        myresult = "[]"
    print(len(myresult))
    my_file2 = open(pathDomain + '/filter.txt', 'w')
    my_file2.write(myresult)
    my_file2.close()
    parselist = json.loads(myresult)
    if len(parselist) > 0:
        ts_arr = []
        for unikal in parselist:
            ts_arr.append(unikal["file_url"])
        arr_len = len(ts_arr)
        # todo Здесь изменено порог с 100 до 10
        if arr_len > 9:
            squar_arr = int(arr_len / 3)  # round down

            i = 0
            while i < squar_arr:
                first_content = getparse(ts_arr[i], validPath)
                if len(first_content) > 1400:
                    first_unikal = isunikal_text(first_content)
                    break
                i = i + 1
            else:
                first_unikal = False

            i = squar_arr
            while i < (arr_len - squar_arr):
                medium_content = getparse(ts_arr[i], validPath)
                if len(medium_content) > 1400:
                    medium_unikal = isunikal_text(medium_content)
                    break
                i = i + 1
            else:
                medium_unikal = False

            i = arr_len - 1
            while i > (arr_len - squar_arr):
                last_content = getparse(ts_arr[i], validPath)
                if len(last_content) > 1400:
                    last_unikal = isunikal_text(last_content)
                    break
                i = i - 1
            else:
                last_unikal = False
        else:
            first_unikal = medium_unikal = last_unikal = False
        result = [first_unikal, medium_unikal, last_unikal]
    else:
        result = [False, False, False]
    my_file.close()

    print("Load filter.txt")
    return result
