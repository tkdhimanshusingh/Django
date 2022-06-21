from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context={
        "variable1":"Himanshu is Great",
        "variable2":"Harry is Great"
    }
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
    #return HttpResponse("This is about page")
def services(request):
    return render(request,'services.html')
    #return HttpResponse("This is Services page")
def contact(request):
    return render(request,'contact.html')
    #return HttpResponse("This is Contact page")