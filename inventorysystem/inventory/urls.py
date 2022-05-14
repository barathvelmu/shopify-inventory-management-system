from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "inventory"),
    path('add-inventory', views.add_inventory, name = "add-inventory"), 
    path('edit-inventory/<int:id>', views.edit_inventory, name = "edit-inventory"), 
    path('delete-inventory/<int:id>', views.delete_inventory, name = "delete-inventory"), 
]