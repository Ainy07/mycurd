from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from . models import User


# Create your views here

def signup(request):
    return render(request,"signup.html")

# create signup form
def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        address = request.POST['address']
        DOB = request.POST['DOB']
        contact = request.POST['contact']
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already exists")
        elif User.objects.filter(contact=contact).exists():
            messages.error(request,"contact already exists")
        else:
            User.objects.create(name=name,email=email,contact=contact,DOB=DOB,password=password,address=address)
        return redirect("/login/")
    


def login(request):
    return render(request,'login.html')    

# create login form
def login_form(request):
    if request.method =='POST':
        contact = request.POST['contact']
        user_password = request.POST['password']
        if User.objects.filter(contact=contact).exists():
           obj = User.objects.get(contact=contact)
           password = obj.password
           if check_password(user_password, password):
                return redirect("/table/")
           else:
            return HttpResponse('password incorrect')
    else:
        return HttpResponse("phone number is not registered")
        
def table(request):
    data = User.objects.all()
    return render(request,'table.html',{"data":data})

#create edit button

def update_view(request, uid):
    res=User.objects.get(id=uid)
    return render(request,'update.html',{'person':res})

#use update data
def update_form_data(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        DOB = request.POST['DOB']
        contact = request.POST['contact']
        User.objects.filter(id=uid).update(name=name,email=email,contact=contact,DOB=DOB,address=address)
        return redirect('/table/')
    
#create delete button
def delete(request,pk):
    use = User.objects.filter(id=pk).delete()
    return redirect('/table/')