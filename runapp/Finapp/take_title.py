import codecs
import traceback
from bs4 import BeautifulSoup

from runapp.ContinueApp.parse_validate_content import getcodname


def get_title(path_to_file):
    # global pos3, codectext
    '''
    try:
        with codecs.open(path_to_file, encoding='utf-8', errors='replace') as my_file:
            # my_file = open(file_path, 'r')
            test_string = my_file.read()
            test_string = test_string.lower()
            my_file.close()
        pos3 = test_string.find("charset=") + 8
        pos4 = test_string.find('"', pos3)
        codectext = test_string[pos3:pos4]
    except BaseException as error:
        # response = HttpResponse("<h3>2.Ошибка " + method + " </h3>")
        full_traceback = traceback.format_exc()
        print(full_traceback)
    if pos3 == 7:
        codectext = "utf-8"
    '''
    codectext = getcodname(path_to_file)
    if codectext == "tf-8":
        print("tf-8 - ",path_to_file)
    print(codectext)
    with codecs.open(path_to_file, encoding=codectext, errors='replace') as my_file:
        my_string = my_file.read()
        my_file.close()
        trace = BeautifulSoup(my_string, "lxml")
        # result_block = trace.findAll("div",{"class": "line"})
        # result_block = trace.find_all("div",class_="line")
        result_block = trace.select('title')
        # print(result_block)
        titlecontent = result_block[0].get_text()

    return titlecontent

