import time

import requests
from bs4 import BeautifulSoup



def get_path_to_folderbjects(file_path):
    path_to_folder = file_path.replace("/home/max/websites", "http://text.seoma.com.ua")
    proxies = None
    # path_to_folder = "htp://text.seoma.com.ua/processing_domain/gsmcenter.ru/period1/forload/folder54.html"
    print(path_to_folder)
    '''
    proxies = {
        'http': 'http://10.18.7.6:3128',
        'https': 'http://10.18.7.6:3128',
    }
    if not isproxy:
        proxies = None
    '''
    url = "https://ru.megaindex.com/a/tcategories?domain=" + path_to_folder
    headers = {
        'Content-Type': "text/html",
        'Accept-Charset': "utf-8",
        'Cache-Control': "no-cache",
    }

    print("Снова Проверяем: " + url)
    time.sleep(3)
    try:
        response = requests.get(url=url, timeout=5000, headers=headers, proxies=proxies)
    except requests.exceptions.ConnectionError:
        time.sleep(3)
        response = requests.get(url=url, timeout=10000, headers=headers, proxies=proxies)
    trace = BeautifulSoup(response.text, "lxml")
    # result_block = trace.findAll("div",{"class": "red"})
    # result_block = trace.find_all("div",class_="line")
    result_block = trace.select('div a[target="_blank"]')
    test_block = trace.findAll("div", {"class": "red"})
    if test_block:
        print("Error path :", file_path)
        return "Error subtitle"
    # print(result_block)
    foldersubject = result_block[0].get_text()
    '''
    domain_dir = "/home/max/websites/fresh_content/all_subjects/" + foldersubject
    if not os.path.exists(domain_dir):
        os.makedirs(domain_dir)
    print("Tree")
    # result = int(tark.split('.')[0])
    '''
    return foldersubject