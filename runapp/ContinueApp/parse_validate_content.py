import codecs
import os
import time
import traceback
import requests
from bs4 import BeautifulSoup
from runapp.ContinueApp.format_html_to_txt import formahtm1totxt
from runapp.ContinueApp.format_text import format_cut_content


def getparse(url_name, save_path):
    # sudo wayback_machine_downloader http://fledur.org.ua:80/2008/02/08/jeto-vy-mozhete-seks-igrushki-svoimi.html -e-d /home/max/websites/Processing_Domain/fledur.org.ua/Period1
    # os.system('/usr/local/bin/wayback_machine_downloader ' + name_url + ' -f ' + str(timstamp_num) + ' -d ' + DomainDir)
    path_to_file = save_path

    osresult = os.system('/usr/local/bin/wayback_machine_downloader ' + url_name + ' -d ' + save_path)
    print(osresult)
    # Обрезаем урл до  первого одинарного слеша для определения пути к файлу
    str = url_name
    fil = str.replace("://","")
    pos = fil.find('/')
    pos2 = fil.rfind('/') + 1
    file_path = save_path + fil[pos:]
    file_name = fil[pos2:]
    print("функция :", "getparse")
    print("Имя файла :", file_name)
    print("Путь : ", path_to_file)
    if os.path.exists(file_path):
        try:
            with codecs.open(file_path, encoding='utf-8', errors='replace') as my_file:
                # my_file = open(file_path, 'r')
                test_string = my_file.read()
                test_string = test_string.lower()
                my_file.close()
            pos3 = test_string.find("charset=") + 8
            pos4 = test_string.find('"',pos3)
            codectext = test_string[pos3:pos4]
        except BaseException as error:
            # response = HttpResponse("<h3>2.Ошибка " + method + " </h3>")
            full_traceback = traceback.format_exc()
            print(full_traceback)
        if pos3 == 7:
            codectext = "utf-8"
        print(codectext)
        with codecs.open(file_path, encoding=codectext, errors='replace') as my_file:
        # my_file = open(file_path, 'r')
            my_string = my_file.read()
            my_file.close()
        my_file2 = open(save_path + '/' + file_name, 'w')
        my_file2.write(my_string)
        my_file2.close()
        my_result = formahtm1totxt(my_string)
        second_format = format_cut_content(my_result,url_name)
    else:
        second_format = "NoContent"
    return second_format


# todo проверка уникальности
def isunikal_text(text_content):
    cutcontent = text_content[:1477]
    proxies = None
    '''
    proxies = {
        'http': 'http://10.18.7.6:3128',
        'https': 'http://10.18.7.6:3128',
    }
    if not isproxy:
        proxies = None
    '''
    url = "http://ahumor.org.ua/textapi.php?text=" + cutcontent
    headers = {
        'Content-Type': "text/xml",
        'Accept-Charset': "utf-8",
        'Cache-Control': "no-cache",
    }
    # time.sleep(3)
    if len(url) < 39:
        print("Проверяем: " + url)
        cutcontent = text_content[:1477]
        url = "http://ahumor.org.ua/textapi.php?text=" + cutcontent
        print("Снова Проверяем: " + url)
    response = requests.get(url=url, headers=headers, proxies=proxies)
    time.sleep(2)
    trace = BeautifulSoup(response.text, "lxml")
    result_block = trace.find('p')
    tark = result_block.get_text()
    result = int(tark.split('.')[0])
    print("Уникальность: ", result)
    if result > 89:
        return True
    else:
        return False
