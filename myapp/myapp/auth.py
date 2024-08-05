from django.shortcuts import redirect ,render
from authModel.models import Authdata

def formview(request) : 
    return render(request ,'index.html')


def insertfunc(request): 
    if request.method =="POST" :
        uname = request.POST["name"]
        uemail = request.POST["email"]
        upassword = request.POST["pass"]
        userdata = Authdata.objects.create(name=uname,email = uemail, password= upassword)
        userdata.save()
        return redirect('/homePage/')
        
