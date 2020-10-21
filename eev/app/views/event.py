from django.shortcuts import render

from django.shortcuts import redirect


def event(request):
    context = {}
    return render(request, 'app/event.html', context)