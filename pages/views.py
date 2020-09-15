from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices,state_choices,bedrooms_choices

def home(request):
    latest_listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context={
       'listings':latest_listings,
       'state_choices':state_choices,
       'price_choices':price_choices,
       'bedrooms_choices':bedrooms_choices,
    }
    return render(request,'pages/home.html',context)

def about(request):
    sotm=Realtor.objects.get(is_mvp=True)
    realtors=Realtor.objects.order_by('-name')
    context={
        'sotm':sotm,
        'realtors':realtors,
    }
    return render(request,'pages/about.html',context)   

