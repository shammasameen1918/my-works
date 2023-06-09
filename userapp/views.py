from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import userform

# Create your views here.
def home(request):
    return render(request,'dashboard.html')

def read(request):
    data = userform.objects.all()
    print(data)
    return render(request,'show.html',{"value":data})

def chart(request):
    # data = userform.objects.all()
    # print(data)
    return render(request,'chart.html')

def rad(request):
    
    
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']
        data = userform.objects.create(email=email,password=password)
        print(data)
         
    else:
        data = userform.objects.all()
        print(data)
    return render(request,'tabl.html',{"value":data})


#def update(request, id):
 #   book = userform.objects.get(id=id)
  #  form = userform(initial={'email': book.email, 'passwoed':book.password})
   # if request.method == "POST":
    #    form = userform(request.POST, isinstance=book)
     #   if form.is_valid():
      #      form.save()
       #     return redirect('/show')
    # return render(request,'edit.html',{'form':form}) 
    
     
def destroy(request,id):
    emp = userform.objects.get(id=id)
    emp.delete()
    return redirect('/show')

def Edit(request , id):
    details = userform.objects.get(id=id)
    return render (request, 'retrive.html' , {"details" : details})

def update(request ,id):
    details = userform.objects.get(id=id)
    if request.method == 'POST' :
        details.email = request.POST['email']
        details.password = request.POST['password']
        details.save()
        return redirect ("/show")
              