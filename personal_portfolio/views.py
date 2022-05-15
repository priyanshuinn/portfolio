from django.shortcuts import redirect, render
from portfolio.models import ContactUS
from django.contrib import messages
import logging

log = logging.getLogger(__name__)

def home_page(request):
    if request.method =='POST':
        print("******************************")
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        contact = ContactUS(name=name,message=message,email=email,subject=subject)
        contact.save()      
        messages.success(request, "Thank you for showing your intrest, your response has been recorded. I'll get back to you very soon.")
        return redirect("/#contact_us")
    
    return render(request, 'home.html')

def about_page(request):
    return render(request, 'about.html')

def service_page(request):
    return render(request, 'services.html')
