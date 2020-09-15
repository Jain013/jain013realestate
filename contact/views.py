from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail
from .models import Contact
from django.utils import timezone



def contact(request):
    if request.method == 'POST':
        listing_id= request.POST.get('listing_id')
        user_id=request.POST.get('user_id')
        listing_title=request.POST.get('listing')
        phone=request.POST.get('phone')
        realtor_email=request.POST.get('realtor_email')
        user_email=request.POST.get('email')
        message=request.POST.get('message')
        name=request.POST.get('name')
        if request.user.is_authenticated:
            if Contact.objects.filter(user_id=user_id,listing_id=listing_id).exists():
              messages.error(request," Already inquired For this Property ")
              return redirect('/listings/'+listing_id)
        
        inquiry=Contact(listing=listing_title,listing_id=listing_id,phone=phone,email=user_email,message=message,user_id=user_id,name=name,contact_date=timezone.now())
        inquiry.save()
     #  send_mail('Listing Requiry','There is an inquiry for ' + listing_title + ' logon to adminpanel for more info','jainjitu86@gmail.com',[realtor_email,'jain.6@iitj.ac.in'],fail_silently=False)
        messages.success(request,'Your inquiry is submitted u will hear soon from our realtor')
        return redirect('/listings/'+listing_id)
            

           
         
        



