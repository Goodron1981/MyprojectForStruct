import traceback
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from runapp.mainapp.runner import main_run

'''
from runapp.add_isue_attribute.search_keys import add_keys_img
from runapp.mainapp.compliter import complete
from runapp.mainapp.finisher import finish
from runapp.mainapp.starter import startfirst
from testpage.models import Urls
from runapp.add_isue_attribute.list_admin import add_last_key
'''


def startpage(request):
    if request.method == 'POST':
        pk=request.POST['but']
        if pk == 'start':
            return render(request, 'runapp/startpage.html',{'shuffl':datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")})
        else:
            return render(request, 'runapp/startpage.html')
    else:
        return render(request, 'runapp/startpage.html')

def startinfo(request):
    if request.method == 'GET':
        res = request.GET.get('status')
        method = request.GET.get('name')
        if res == 'start':

            # complete()
            response =  HttpResponse("<h3>1. Начало " + method + " !</h3>")

        else:
            try:
                if method == 'Load':
                    main_run()
                    '''
                elif method == 'Key':
                    add_keys_img()
                elif method == 'Add':
                    complete()
                elif method == 'Close':
                    finish()
                    '''
                response = HttpResponse("<h3>2.Окончание " + method + " </h3>")
            except BaseException as error:
                response = HttpResponse("<h3>2.Ошибка " + method + " </h3>")
                full_traceback = traceback.format_exc()
                print(full_traceback)
            # response = render(request,'runapp/phone-filter.html', {'phonenumbers':queryset})
    return response