import re
import sys
from django.shortcuts import render, redirect
from django.urls import reverse

def index_view(request):
    return render(request, 'index.html')

def home_view(request):
    return render(request,'home.html')

def compiler_view(request):
    codeareadata = ''
    output = ''
    if request.method == "POST":
        codeareadata = request.POST.get('codearea')

        try:
            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(codeareadata)
            sys.stdout.close()
            sys.stdout = original_stdout
            output = open('file.txt', 'r').read()

        except Exception as e:
            sys.stdout = original_stdout
            output = str(e)

    return render(request, 'compiler.html', {"code": codeareadata, "output": output})

def contact_us_view(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')

        data = f" name: {name}\n Email Address: {email}\n Phone: {phone}\n Message: {message}\n\n\n"

        w = open('contact.txt', 'a')
        w.write(data)

    return render(request, 'contact_us.html')

def about_us_view(request):
    return render(request, 'about_us.html')
