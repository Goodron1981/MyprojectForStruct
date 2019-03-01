import codecs
import json
import os
import time

from runapp.ContinueApp.parse_validate_content import getcodname


def loadarhivpage(nameDomain):
    # DomainDir = nameDomain.replace("http://", "/home/max/websites/processing_domain/")
    DomainDir = "/home/max/websites/processing_domain/" + nameDomain
    print(DomainDir)
    #directory = os.path.dirname(DomainDir)
    if not os.path.exists(DomainDir):
        os.makedirs(DomainDir)

    # os.system("wayback_machine_downloader -l -o '/\.(html|htm)$/i' " + nameDomain + "  > list.txt")
    # os.system('/usr/local/bin/wayback_machine_downloader -l-d /home/max/websites/fledur.org.ua -o "/\.(html|htm)$/i" http://fledur.org.ua > /home/max/Рабочий стол/ForProjects/myproject/list.txt')

    print('Процесс: loadarhivpage')
    foop  = os.system('/usr/local/bin/wayback_machine_downloader -l -o "/\.(html|htm)$/i" ' + nameDomain + ' > "' + DomainDir + '/listimstamps.txt"')
    # foop = os.system('/usr/local/bin/wayback_machine_downloader -l -o "/\.(html|htm)$/i" ' + nameDomain)
    if foop > 0:
        nameDomain = "https://" + nameDomain
        foop = os.system('/usr/local/bin/wayback_machine_downloader -l -o "/\.(html|htm)$/i" ' + nameDomain + ' > "' + DomainDir + '/listimstamps.txt"')
        print("2 попытка ",foop)
    # print('/usr/local/bin/wayback_machine_downloader -l -o "/\.(html|htm)$/i" ' + nameDomain + ' > "' + DomainDir +
    #  '/listimstamps.txt"')
    time.sleep(5)
    file_path = DomainDir + '/listimstamps.txt'
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

    # my_string = my_file.read()
    print(len(my_string))
    # todo переделать поиск по начальной ]и [ с конца.
    '''
    stratarr = my_string.find("{")
    if stratarr > 0:
        finarr = my_string.rfind("}")+1
        my_arr = my_string[stratarr:finarr]
        result = "[" + my_arr + "]"
    else:
        result = "[]"
    '''
    stratarr = my_string.rfind("]")
    finarr = my_string.rfind("[",0,stratarr)
    result = my_string[finarr+1:stratarr+1]
    testarr = result.find("{")
    if testarr > 0:
        finuarr = result.rfind("}") + 1
        my_arr = result[testarr:finuarr]
        myresult = "[" + my_arr + "]"
    else:
        myresult = "[]"
    print(len(myresult))
    my_file2 = open(DomainDir + '/Filter.txt', 'w')
    my_file2.write(myresult)
    my_file2.close()
    parselist = json.loads(myresult)
    print(json.dumps(parselist, indent=4))
    my_file.close()
    print('load oll by: ', nameDomain)
    return parselist
