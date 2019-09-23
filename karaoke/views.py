from django.shortcuts import render


# Create your views here.
context = {
    'nomes':[
        'eric',
        'bruno',
        'camila'
    ],
    'vazio': False,
    'teste': 'teste'}
def index(request):
    return render(request, 'index.html', context)