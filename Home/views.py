from django.shortcuts import render,HttpResponse
from datetime import datetime
from Home.models import Contact

def index(request):
    #return HttpResponse("This is homepage")
    return render(request,'index.html')

def subjects(request):
    #return HttpResponse("This is subjects page")
    #return HttpResponse("This is homepage")

    return render(request,'subjects.html')

def source_code(request):
    #return HttpResponse("This is source code")
    return render(request,'source_code.html')

def contribute(request):
    #return HttpResponse("This is contribute page")
    return render(request,'contribute.html')

def about_us(request):
    #return HttpResponse("This is About Us page")
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        #datetime.today()
        contact=Contact(name=name,email=email,message=message,date=datetime.today())
        contact.save()
        
    #return HttpResponse("This is Contact Us page")
    return render(request,'contact.html')

def tandc(request):
    #return HttpResponse("This is Terms and Condition  page")
    return render(request,'tandc.html')

def privacyandpolicy(request):
    #return HttpResponse("This is Privacy and Policy page")
    return render(request,'privacyandpolicy.html')

