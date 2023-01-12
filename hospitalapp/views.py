from django.shortcuts import render
from.models import Department,Doctors
from.forms import Bookingform

# Create your views here.
def index(request):
    
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def booking(request):
    if request.method=="POST":
        form=Bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render (request,'confirmation.html')

    formvb=Bookingform()
    dict_book={
        'book':formvb
    }
    return render(request,'booking.html',dict_book)
def contact(request):
   
    return render(request,'contact.html')
def department(request):
    dict_dip={
        'dep':Department.objects.all()
     }

    return render(request,'department.html',dict_dip)
def doctors(request):
    dict_doc={
        'doc':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_doc)        
    