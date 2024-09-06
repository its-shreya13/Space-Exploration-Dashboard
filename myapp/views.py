from django.shortcuts import render, redirect
from myapp.models import Contact

def hello_world(request):
    return render(request,'home.html')

def contact(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        data = Contact(email=email, password=password)
        data.save()
        return redirect('hello_world')  # Redirect to the hello_world view which renders home.html
    
    return render(request, 'form.html')

def satellite_position(request):
    return render(request, 'sp.html')

def upcoming_launches(request):
    return render(request, 'ul.html')

def astronomical_picture(request):
    return render(request, 'aopd.html')

def about(request):
    return render(request, 'about.html')
def quiz(request):
    return render(request,'quiz.html')
