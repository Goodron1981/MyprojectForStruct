from django.db import models
from django.contrib import admin

class Excludespage(models.Model):
    ex_page= models.CharField(max_length=100, default = 'None', verbose_name= 'Исключающие страницу')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

class ExcludespageAdmin(admin.ModelAdmin):
    list_display = ('ex_page', 'create_date')
    ordering = ('id',)

class Excludestate(models.Model):
    ex_state= models.CharField(max_length=100, default = 'None', verbose_name= 'Исключающие предложение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

class ExcludestateAdmin(admin.ModelAdmin):
    list_display = ('ex_state', 'create_date')
    ordering = ('id',)
    search_fields = ('ex_state',)