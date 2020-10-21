from django.shortcuts import render

from django.shortcuts import redirect

from django.views.decorators.csrf import csrf_exempt

import requests

@csrf_exempt
def login_page(request):
    context = {}
    if request.method == 'POST':
        r = requests.post('http://127.0.0.1:8000/api/v1/login/', data=request.POST)
        if r.status_code == 200:
            response = r.json()
            token = response['token']
            print(token)
            print("well done 200 code")
        elif r.status_code == 400:
            print("bad credentials")
        else:
            print("something went wrong")
        # return redirect('home')
    return render(request, 'app/login.html', context)

@csrf_exempt
def register_page(request):
    context = {}
    if request.method == 'POST':
        r = requests.post('http://127.0.0.1:8000/api/v1/users/', data=request.POST)
        # print(r.json())
    return render(request, 'app/register.html', context)

def password_forgot(request):
    context = {}
    return render(request, 'app/password_forgot.html', context)