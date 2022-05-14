from django.contrib import admin
from .models import Inventory, Warehouse

# To handle data through Django Admin Interface (testing purposes)
admin.site.register(Inventory)
admin.site.register(Warehouse)
