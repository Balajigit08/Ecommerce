from django.contrib import admin
from .models import *
# Register your models here.

# class CatagoryAdmin(admin.ModelAdmin):
#     list_display = ('name','image','description')
# admin.site.register(catagory,CatagoryAdmin)

admin.site.register( Category)
admin.site.register(Product)
