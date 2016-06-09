from django.contrib import admin
from Product.models import Products, Orders, Workers


# Register your models here.
admin.site.register(Products);
admin.site.register(Orders);
admin.site.register(Workers);
