'''
from runapp.sape.load_isue import load_isue_sape
from runapp.rota.load_isue import load_isue_rota
from runapp.add_isue_attribute.parse_atrributes import parser_attr
from runapp.add_isue_attribute.search_keys import add_keys_img
from runapp.rota.sort_isue import sortallisues
'''
from runapp.mainapp.LoadData import loaddata
from runapp.mainapp.valid_as_new import validnewdomain

def main_run():
    print('В runner')
    newdomainlist = loaddata('NewDomens.xlsx')
    olddomainlist = loaddata("OldDomens.xlsx")
    validnewdomain(newdomainlist, olddomainlist)

    print('Успешный выход из runner')

    '''
    sortallisues()
    load_isue_sape()
    load_isue_rota()
    parser_attr()
    '''