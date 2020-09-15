from django.contrib import admin
from .models import Listing

class AdminListing(admin.ModelAdmin):
    list_display=('id','title','is_published','list_date','price','realtor')
    list_display_links=('title',)
    list_filter=('realtor','list_date')
    list_editable=('is_published',)
    search_fields=('title','city','state','price')
    list_per_page=25

# Register your models here.
admin.site.register(Listing,AdminListing)
