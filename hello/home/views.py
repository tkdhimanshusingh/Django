from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context={
        "variable1":"Himanshu is Great",
        "variable2":"Harry is Great"
    }
    return render(request,'index.html',context)
def about(request):
    return HttpResponse("This is about page")
def services(request):
    return HttpResponse("This is Services page")
def contact(request):
    return HttpResponse("This is Contact page")