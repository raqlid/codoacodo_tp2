from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    context = {
        'username': 'Walter',
        'edad': 29
    }
    return render(request, 'app/index.html', context)