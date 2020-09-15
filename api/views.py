from listings.models import Listing
from realtors.models import Realtor
from contact.models import Contact

from api.serializers import ListingSerializer,RealtorSerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_root(request,format=None):
    return Response({
       'listings': reverse('listing-list',request=request,format=format),
       'realtors': reverse('realtor-list',request=request,format=format),
    })

class ListingsList(generics.ListCreateAPIView):
    queryset=Listing.objects.all()
    serializer_class=ListingSerializer

class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Listing.objects.all()
    serializer_class=ListingSerializer

class RealtorsList(generics.ListCreateAPIView):
    queryset=Realtor.objects.all()
    serializer_class=RealtorSerializer

class RealtorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Realtor.objects.all()
    serializer_class=RealtorSerializer

