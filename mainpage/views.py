from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'nomer_okoshka': '9 и 3/4',
        'name': 'Гараж'} # добавили для index.html
    return render(
        request,               #Запрос
        'mainpage/index.html', # путь к шаблону
        context                # подстановки словарь
    )
    