from django.shortcuts import render

from django.shortcuts import redirect


def home(request):
    context = {}
    return render(request, 'app/home.html', context)