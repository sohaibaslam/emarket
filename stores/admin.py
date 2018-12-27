from django.contrib import admin
from . import models


@admin.register(models.Store)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    pass
