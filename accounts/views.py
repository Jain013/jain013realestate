from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contact.models import Contact

def register(request):
   if request.method == 'POST':
      first_name=request.POST.get('first_name')
      last_name=request.POST.get('last_name')
      username=request.POST.get('username')
      email=request.POST.get('email')
      password=request.POST.get('password')
      password2=request.POST.get('password2')
      if password == password2:
         invalid_credentials=0
         if User.objects.filter(username=username).exists():
            messages.error(request,'username is already taken')
            invalid_credentials=1
         if User.objects.filter(email=email).exists():
            messages.error(request,'email is already in use')
            invalid_credentials=1
            
         if not invalid_credentials:
            user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            user.save()
            messages.success(request,'Successfully Registered')
            return redirect('pages:home')          
      else:
         messages.error(request,'passwords mismatch')
      return redirect('accounts:register')      
   else:  
     return render(request,'accounts/register.html')

def login(request):
   if request.method == 'POST':
      username=request.POST.get('username')
      password=request.POST.get('password')
      user=auth.authenticate(username=username,password=password)
      if user is not None:
         auth.login(request,user)
         return redirect('accounts:dashboard')
      else:
        messages.error(request,'Invalid credentials')
        return redirect('accounts:login')   
   else:
      return render(request,'accounts/login.html')     

def dashboard(request):
   inquiries=Contact.objects.filter(user_id=request.user.id).order_by('-contact_date')
   return render(request,'accounts/dashboard.html',{'inquiries':inquiries})

def logout(request):
   auth.logout(request)
   return redirect('accounts:login')

