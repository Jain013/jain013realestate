from django.shortcuts import render,get_object_or_404
from .models import Listing
from realtors.models import Realtor
from django.core.paginator import Paginator
from listings.choices import price_choices,state_choices,bedrooms_choices

def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)
    for listing in listings:
        print('hello')
        print(listing.list_date)
    paginator=Paginator(listings,2)
    page_number=request.GET.get('page')
    page_listings=paginator.get_page(page_number)
    context={
        'listings':page_listings
    }
    return render(request,'listings/listings.html',context)

def listing(request,listing_id):
    listing=Listing.objects.get(pk=listing_id)
    context={
        'listing': listing,
    }
    return render(request,'listings/listing.html',context)

def search(request):
   queryset_list = Listing.objects.order_by('-list_date')

   if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
       queryset_list = queryset_list.filter(description__icontains=keywords)
   if 'city' in request.GET:
    city = request.GET['city']
    if city:
       queryset_list = queryset_list.filter(city__iexact=city)

   if 'state' in request.GET:
    state = request.GET['state']
    if state:
       queryset_list = queryset_list.filter(state__iexact=state)
 
   if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
       queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

   if 'price' in request.GET:
    price = request.GET['price']
    if price:
       queryset_list = queryset_list.filter(price__lte=price)
   
   context={
       'listings':queryset_list,
       'values':request.GET,
       'state_choices':state_choices,
       'price_choices':price_choices,
       'bedrooms_choices':bedrooms_choices,
    }
   return render(request,'listings/search.html',context)



