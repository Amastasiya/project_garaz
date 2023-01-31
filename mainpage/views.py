from django.shortcuts import render
from .models import Employee
from .models import Guide
from django.http import HttpResponse

import json

# Create your views here.
def index(request):
    if request.method == 'POST':

        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        print(body_data)
        a_value = 996677
        return HttpResponse(json.dumps(
            {"a_field": a_value}
        ))
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

