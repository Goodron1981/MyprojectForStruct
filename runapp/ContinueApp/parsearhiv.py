import json
import os


def loadarhivpage(nameDomain):
    DomainDir = nameDomain.replace("http://", "/home/max/websites/Processing_Domain/")
    #directory = os.path.dirname(DomainDir)
    if not os.path.exists(DomainDir):
        os.makedirs(DomainDir)

    # os.system("wayback_machine_downloader -l -o '/\.(html|htm)$/i' " + nameDomain + "  > list.txt")
    # os.system('/usr/local/bin/wayback_machine_downloader -l-d /home/max/websites/fledur.org.ua -o "/\.(html|htm)$/i" http://fledur.org.ua > /home/max/Рабочий стол/ForProjects/myproject/list.txt')

    print('Процесс: loadarhivpage')
    foop  = os.system("/usr/local/bin/wayback_machine_downloader -l -o '/\.(html|htm)$/i' " + nameDomain + ' > "' + DomainDir + '/listimstamps.txt"')

    my_file = open(DomainDir + '/listimstamps.txt', 'r')
    my_string = my_file.read()
    print(len(my_string))
    my_arr = my_string.split('[')
    result = None
    parselist = None
    if my_arr[1]:
        result = '[' + my_arr[1]
        result = result.replace(',\n]', ']')
        print(len(result))
        my_file2 = open(DomainDir + '/Filter.txt', 'w')
        my_file2.write(result)
        my_file2.close()
        parselist = json.loads(result)
    # print(json.dumps(parselist, indent=4))
    my_file.close()
    print('load oll by: ', nameDomain)
    return parselist
