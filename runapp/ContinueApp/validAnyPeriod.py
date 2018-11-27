import os
import json
from runapp.ContinueApp.parse_validate_content import getparse
from runapp.ContinueApp.parse_validate_content import isunikal_text


def isunikalPeriod(firstyear, lastyear, Domain, pathDomain):
    # DomainDir = Domain.replace("http://", "/home/max/websites/Processing_Domain/")
    # directory = os.path.dirname(DomainDir)
    if not os.path.exists(pathDomain):
        os.makedirs(pathDomain)
    validPath = pathDomain + "/ForValid"
    if not os.path.exists(validPath):
        os.makedirs(validPath)

    print('Процесс: isunikalPeriod')
    os.system("/usr/local/bin/wayback_machine_downloader -l -o '/\.(html|htm)$/i' " + Domain + ' -f ' + str(
        firstyear) + ' -t ' + str(lastyear) + '> "' + pathDomain + '/listimstamps.txt"')
    print("Загружено с ", firstyear, " по ", lastyear)
    my_file = open(pathDomain + '/listimstamps.txt', 'r')
    my_string = my_file.read()
    print(len(my_string))
    my_arr = my_string.split('[')
    result = None
    parselist = None
    if my_arr[1]:
        result = '[' + my_arr[1]
        result = result.replace(',\n]', ']')
        print(len(result))
        my_file2 = open(pathDomain + '/Filter.txt', 'w')
        my_file2.write(result)
        my_file2.close()
        parselist = json.loads(result)
    if parselist:
        ts_arr = []
        for unikal in parselist:
            ts_arr.append(unikal["file_url"])
        arr_len = len(ts_arr)
        if arr_len > 99:
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

    print("Load Filter.txt")
    return result
