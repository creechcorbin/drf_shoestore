from django.contrib import admin
from shoestore.models import Shoe, Manufacturer

# Register your models here.

admin.site.register(Shoe)
admin.site.register(Manufacturer)