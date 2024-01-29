from django.contrib import admin
from .models import Product, Order
from django.contrib.auth.models import Group 


# to have your on title at the admin page
admin.site.site_header = 'Revelation Dashboard'

# To list your products on the dashboard so it displays well
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ['category']
    
# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
# To unregister a group at the admin panel
#admin.site.unregister(Group)