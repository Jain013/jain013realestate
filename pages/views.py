from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices,state_choices,bedrooms_choices

def home(request):
    try:
      latest_listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    except Listing.DoesNotExist:
       latest_listings= None   
    context={
       'listings':latest_listings,
       'state_choices':state_choices,
       'price_choices':price_choices,
       'bedrooms_choices':bedrooms_choices,
    }
    return render(request,'pages/home.html',context)

def about(request):
    try:
       sotm=Realtor.objects.get(is_mvp=True)
    except Realtor.DoesNotExist:
       sotm = None
    try:   
       realtors=Realtor.objects.order_by('-name')
    except Realtor.DoesNotExist:
       realtors=None

    context={
        'sotm':sotm,
        'realtors':realtors,
    }
    return render(request,'pages/about.html',context)   

