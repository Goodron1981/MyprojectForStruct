import os


def getownerlist(last_url, name_domain):
    DomainDir = name_domain.replace("http://", "/home/max/websites/")
    name_url = last_url["file_url"]
    timstamp_num = last_url["timestamp"]
    os.system('/usr/local/bin/wayback_machine_downloader ' + name_url + ' -f ' + str(timstamp_num) + ' -d ' + DomainDir)
    # wayback_machine_downloader http://fledur.org.ua:80/52646-zamerzshaya-iz-majami-new-in-town-2009-bdrip-hq.html -f 20091215175817 -d DomainDir
    print("выгружено список")

