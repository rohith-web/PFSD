from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render
from django.contrib import messages

from .models import Admin, Register
from django.contrib import messages

# Create your views here.
def ttmhome(request):
    return render(request, "ttmhome.html")

def checkadminlogin(request):
    print(">>>>>>>>1" + request.method)
    if request.method == "POST":
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        flag=0
        flag = Register.objects.filter(username=uname,password=pwd).values()
        print("flag = ",flag)
        print(">>>>>>>>>" + uname + ":" + pwd)

        if flag:
            print(">>>>>>>>>"+ uname)
            if uname == "1":
                messages.info(request,"This is Admin Home Page")
                return render(request,"adminhome.html")
        if flag:
            messages.info(request, "This is Users Home Page")
            return render(request, "ttmhome.html")
        else:
            messages.info(request, "Your Credentials are not Correct")
            return render(request,"loginfail.html")

def checkregistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        addr = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        if pwd == cpwd:
            if Register.objects.filter(username=uname).exists():
                messages.info(request,"username taken...")
                return render(request,"register.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request,"email taken...")
                return render(request,"register.html")
            else:
                user = Register.objects.create(name=name, address=addr, email=email, phno=phno, username=uname,
                                             password=pwd)
                user.save()
                messages.info(request, "user created...")
                return render(request,"Login.html")
        else:
            messages.info(request, "password is not matching...")
            return render(request, "register.html")


def viewplaces(request):
    data = Packages.objeccts.all()
    return render(request,"viewsplaces",{"placesdata":data})
def checkchangepassword(request):
    if request.method == "POST":
        uname= request.POST["uname"]
        opwd = request.POST["opwd"]
        npwd = request.POST["npwd"]
        flag=Register.objects.filter(username=uname,password=opwd).values()
        #filter-> It is use to compare the HTML data with table Row
        if flag:
            Register.objects.filter(username=uname,password=opwd).update(password=npwd)
            return render(request,"index.html")
        else:
            return render(request,"changepassword.html")


    return render(request,"changepassword.html")