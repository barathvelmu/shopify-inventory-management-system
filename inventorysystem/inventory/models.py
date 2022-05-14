from django.db import models
from django.utils.timezone import now

# Handles Warehouses (CRUD)
class Warehouse(models.Model):
    name = models.CharField(max_length=250)
    
    # To list objects by "name" in Django Admin (instead of Object 1)
    def __str__(self):
        return self.name

# Handles Inventory Items (CRUD)
class Inventory(models.Model):
    value = models.FloatField() # value of the inventory
    date = models.DateField(default=now) # date the inventory was added
    item = models.TextField() # item name/inventory name
    warehouse = models.CharField(max_length=250) # warehouse the inventory is associated with
    
    # To describe an instance
    def __str__(self):
        return self.warehouse
        
    class Meta:
        ordering = ['-date'] # ordering items by date (descending order)
        verbose_name_plural = "Inventories" # Defining plural naming for Django Admin interface

        
