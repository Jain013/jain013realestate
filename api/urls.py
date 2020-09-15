from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    path('',views.api_root),
    path('listings/',views.ListingsList.as_view(),name='listing-list'),
    path('listings/<int:pk>/',views.ListingDetail.as_view(),name='listing-detail'),
    path('realtors/',views.RealtorsList.as_view(),name='realtor-list'),
    path('realtors/<int:pk>/',views.RealtorDetail.as_view(),name='realtor-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])



