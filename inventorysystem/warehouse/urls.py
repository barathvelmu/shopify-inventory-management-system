from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "warehouse"),
    path('add-warehouse', views.add_warehouse, name = "add-warehouse"), 
    path('edit-warehouse/<int:id>', views.edit_warehouse, name = "edit-warehouse"), 
    path('delete-warehouse/<int:id>', views.delete_warehouse, name = "delete-warehouse"), 
]