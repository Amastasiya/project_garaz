from django.shortcuts import render
from .models import Employee
from .models import Guide

# Create your views here.
def index(request):
    context = {
        'nomer_okoshka': '9 и 3/4',
        'name': 'Гараж', # добавили для index.html
        'employee': Employee.objects.all(),
        'guide': Guide.objects.all(),
        'menu_one': [
            'События',
            'Телефонный справочник',
            'Календарь',
            'История'
        ]
    }

    return render(
        request,               #Запрос
        'mainpage/index.html', # путь к шаблону
        context                # подстановки словарь
    )

