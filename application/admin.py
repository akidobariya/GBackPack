from django.contrib import admin
# from application.models import RegisterData, contactinformation, ShopProduct
from application.models import *

# Register your models here.

admin.site.register(contactinformation)

admin.site.register(RegisterData1)

admin.site.register(ShopProduct)

admin.site.register(cartinfo)