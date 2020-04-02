from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@##$%^&*'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length',12))
    if length > 10:
        length = 10
    for i in range(0,length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html',{'password':thepassword})

def about(request):
    return render(request, 'generator/aboutme.html')
