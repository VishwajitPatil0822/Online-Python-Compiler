import sys
import io
from django.shortcuts import render,redirect
from .models import Contact

def index_view(request):
    return render(request, 'index.html')

def home_view(request):
    return render(request,'python_compiler/home.html')

def compiler_view(request):
    codeareadata = ''
    output = ''

    if request.method == "POST":
        codeareadata = request.POST.get('codearea')

        try:
            buffer = io.StringIO()
            sys.stdout = buffer

            scope = {}
            exec(codeareadata, scope)
            sys.stdout = sys.__stdout__

            output = buffer.getvalue()

        except Exception as e:
            sys.stdout = sys.__stdout__
            output = str(e)

    return render(request, 'python_compiler/compiler.html', {"code": codeareadata, "output": output})

def contact_us_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        data = Contact(name=name, email=email, phone=phone, message=message)
        data.save()
        return redirect('home_view_urls')

    return render(request, 'python_compiler/contact_us.html')

def about_us_view(request):
    return render(request, 'python_compiler/about_us.html')
