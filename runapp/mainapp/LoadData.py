# заливка ключей
import xlrd


def loaddata(filename):
    workbook = xlrd.open_workbook('/home/max/fordomens/' + filename)
    sheet = workbook.sheet_by_index(0)
    my_list = []
    for rowx in range(sheet.nrows):
        cols = sheet.row_values(rowx)
        my_list.append(cols[0])
    print("Список из: ", filename, " - ", my_list)
    return my_list

    '''
1 in my_list

True    
    '''
