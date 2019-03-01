import os

from django.test import TestCase

from runapp.Finapp.loadAllPagePeriod import filter_non_printable
from runapp.Finapp.save_result import save_fresh
from runapp.Finapp.take_subtitle import get_path_to_folderbjects
from chardet.universaldetector import UniversalDetector


# Create your tests here.
from runapp.Finapp.take_text import parsepage
from runapp.Finapp.take_title import get_title


def test():
    loadPath = "/home/max/websites/processing_domain/gsmcenter.ru/period1/forload"
    f = open(loadPath + "/loadlist.txt")
    for line in f.readlines():
        butline = filter_non_printable(line)
        result = get_path_to_folderbjects(butline)
        print(result)


def test2(pather):
    detector = UniversalDetector()
    with open(pather, 'rb') as fh:
        for line in fh:
            detector.feed(line)
            if detector.done:
                break
    detector.close()
    print(detector.result['encoding'])

def test3(loadPath,domain):
    mymass = []
    os.system("find " + loadPath + " -name '*.html' > " + loadPath + "/loadlist.txt")
    print('find ' + loadPath + ' -name "*.html" > ' + loadPath + '/loadlist.txt')
    print("loadlist:")
    f = open(loadPath + "/loadlist.txt")
    for line in f.readlines():
        butline = filter_non_printable(line)
        mymass.append(butline)

    for path in mymass:
        fin_format = parsepage(path)
        if len(fin_format) > 1400:
            category = get_path_to_folderbjects(path)
            title = get_title(path)
            save_fresh(title, fin_format, category, path, domain)

def test4(loadPath,domain):
    mymass = []
    os.system("find " + loadPath + " -name '*.html' > " + loadPath + "/loadlist.txt")
    print('find ' + loadPath + ' -name "*.html" > ' + loadPath + '/loadlist.txt')
    print("loadlist:")
    f = open(loadPath + "/loadlist.txt")
    for line in f.readlines():
        butline = filter_non_printable(line)
        mymass.append(butline)

    for path in mymass:
        category = get_path_to_folderbjects(path)
        print(category)