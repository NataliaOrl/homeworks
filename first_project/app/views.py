import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse


from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    path = r"C:\Users\Natalia\Desktop\Django_Projects\Homeworks\dj-homeworks\1.1-first-project\first_project"
    work_dir = os.listdir(path)
    msg = f'Содержимое рабочей директории: {work_dir}'
    return HttpResponse(msg)

