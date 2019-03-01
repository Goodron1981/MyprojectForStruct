import codecs
import traceback

from runapp.ContinueApp.format_html_to_txt import formathtmltotxt
from runapp.ContinueApp.format_text import format_cut_content
from runapp.ContinueApp.parse_validate_content import getcodname


def parsepage(path_to_file):
    codectext = getcodname(path_to_file)
    print("parsepage codectext: ", codectext)
    with codecs.open(path_to_file, encoding=codectext, errors='replace') as my_file:
        # my_file = open(file_path, 'r')
        try:
            my_string = my_file.read()
        except UnicodeDecodeError as error:
            my_string = "Empty"
            print("Ошибка при чтении файла :", path_to_file)
        my_file.close()
        '''
    global pos3, codectext
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
    print("from parsepage codectext: ", codectext)
    with codecs.open(path_to_file, encoding=codectext, errors='replace') as my_file:
        my_string = my_file.read()
        my_file.close()
        '''
    my_result = formathtmltotxt(my_string)
    second_format = format_cut_content(my_result, path_to_file)
    return second_format