from django.shortcuts import render
from allanisapp.models import Signup
# Create your views here.

def signup(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        phone_number=request.POST.get('phone_number')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')

        customer=Signup(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number,address=address,dob=dob,gender=gender)
        customer.save()

    return render(request,"signup.html")