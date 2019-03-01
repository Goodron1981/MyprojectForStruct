def maker_par_ph(content):
    peacelen = int(len(content) / 3)
    startfirstpart = content.rfind('. ', 0, peacelen)
    finfirstpart = content.find('. ', peacelen)
    # не срабатывает rfind
    renstart = peacelen - startfirstpart
    renfinish = finfirstpart - peacelen
    if renstart - renfinish > 0:
        firstpart = finfirstpart
    else:
        firstpart = startfirstpart

    startsecondpart = content.rfind('. ', peacelen, (peacelen * 2) - 1)
    finsecondpart = content.find('. ', (peacelen * 2) + 1)
    renstart = (peacelen * 2) - startsecondpart
    renfinish = finsecondpart - (peacelen * 2)
    if renstart - renfinish > 0:
        secondpart = finsecondpart
    else:
        secondpart = startsecondpart

    resulttext = '\t' + content[:firstpart + 1] + ' \r\t' + content[firstpart + 2:secondpart + 1] + '\r\t' + content[secondpart + 2:]
    print(resulttext)
    return resulttext
    '''
    my_file2 = open("/home/max/Документы/Обработано", 'w')
    my_file2.write(resulttext)
    my_file2.close()
    '''
