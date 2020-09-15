from rest_framework import serializers
from listings.models import Listing
from realtors.models import Realtor
from contact.models import Contact

class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Listing
        fields=['url','title','price','sqft']


class RealtorSerializer(serializers.HyperlinkedModelSerializer):
    listings=serializers.HyperlinkedRelatedField(many=True,view_name='listing-detail',read_only=True)
    class Meta:
        model=Realtor
        fields=['url','name','email','listings']
