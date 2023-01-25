from django.shortcuts import render
from .models import Employee
from .models import Guide
from django.http import HttpResponse

import json

# Create your views here.
def index(request):
    if request.method == 'POST':
        for elem in request.POST:
            print(elem, request.POST)
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        print(body_data)
        return HttpResponse("<h1>Prosto text</h1>")
    employee = Employee.objects.all()
    context = {
        'nomer_okoshka': '9 и 3/4',
        'name': 'Гараж', # добавили для index.html
        'employee': employee,
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

