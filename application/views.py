from django.shortcuts import render,redirect
from application.models import database
def index(request):
    if request.method=="POST":
        name=request.POST['name']
        number=request.POST['number']
        obj=database()
        obj.Name=name
        obj.Number=number
        obj.save()
        return redirect('index')
    return render(request,'index.html')
