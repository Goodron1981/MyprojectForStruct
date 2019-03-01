'''
from runapp.sape.load_isue import load_isue_sape
from runapp.rota.load_isue import load_isue_rota
from runapp.add_isue_attribute.parse_atrributes import parser_attr
from runapp.add_isue_attribute.search_keys import add_keys_img
from runapp.rota.sort_isue import sortallisues
'''
from runapp.mainapp.LoadData import loaddata
from runapp.mainapp.valid_as_new import validnewdomain
from runapp.For_Metriks.all_function_metriks import mark_start, mark_fin

def main_run():
    print('Начало В runner')
    mark_start()
    newdomainlist = loaddata('NewDomens.xlsx')
    olddomainlist = loaddata("OldDomens.xlsx")
    validnewdomain(newdomainlist, olddomainlist)
    mark_fin()
    print('Успешный выход из runner')

    '''
    sortallisues()
    load_isue_sape()
    load_isue_rota()
    parser_attr()
    '''