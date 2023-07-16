from django.shortcuts import HttpResponse,render
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    context = {
        'variable':"JAIMIN"
    }
    return render(request,'index.html',context)
   # return HttpResponse("this is Home page")

def about(request):
    return render (request,'about.html')
    #return HttpResponse("This is about page")

def services(request):
    return render (request,'request.html')
    #return HttpResponse("This is Service page")

def contact(request):
    if request.method =="POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        desc = request.POST.get("desc")

        contact = Contact(name=name,phone=phone,email=email,desc=desc,date=datetime.today())
        contact.save()

        

    return render(request,'contact.html')