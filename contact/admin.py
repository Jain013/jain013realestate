from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display=('listing_id','user_id','name','email','phone')
    list_display_links=('name',)
    search_fields=('name','user_id')
    list_per_page=25

admin.site.register(Contact,ContactAdmin)


