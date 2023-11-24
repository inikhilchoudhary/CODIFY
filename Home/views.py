from django.shortcuts import render,HttpResponse


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

