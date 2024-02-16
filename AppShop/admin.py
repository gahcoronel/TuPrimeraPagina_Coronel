from django.contrib import admin

# Register your models here.

from AppShop import models

admin.site.register(models.Cliente)
admin.site.register(models.Vendedor)
admin.site.register(models.Producto)
