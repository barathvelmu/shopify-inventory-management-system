from django.shortcuts import render, redirect
from .models import Warehouse, Inventory
from django.contrib import messages
from django.core.paginator import Paginator
import numbers

# Inventory List Page (added Pagination: 10 objects per page)
def index(request):
    inventories = Inventory.objects.all()
    # Pagination:
    paginator = Paginator(inventories, 10) # Second variable specifies "item(s) per page"
    page_number = request.GET.get('page') # Selecting specific page from URL
    page_objects = Paginator.get_page(paginator, page_number) # Reflect all items for a given page
    # Return:
    context = { 'inventories': inventories, 'page_objects': page_objects} # Pass to Views
    return render(request, 'inventory/index.html', context)

# Logic to add an inventory item
def add_inventory(request):    
    warehouses = Warehouse.objects.all()  
    context= { 'warehouses':warehouses, 'entries': request.POST } # 'entries' helps to persist form info (e.g., editing)
    
    if request.method == 'GET':
        return render(request, 'inventory/add_inventory.html', context)
    
    if request.method == 'POST':
        # Get inputs
        value = request.POST.get('value')
        item = request.POST.get('item')
        date = request.POST.get('date')
        warehouse = request.POST.get('warehouse')
        
        # Validate if user has filled mandatory fields
        if None or not (value and item and date and warehouse):
            messages.error(request, "Please fill in all fields :)")
            return render(request, 'inventory/add_inventory.html', context)
    
    # If all is well, save new inventory to the database 
    Inventory.objects.create(value = value, date = date, warehouse = warehouse, item = item)
    messages.success(request, "New inventory item has been added :)")
    return redirect('inventory')

# Logic to edit an inventory item    
def edit_inventory(request, id):
    inventory = Inventory.objects.get(pk=id) # Obtain the particular inventory to be edited
    warehouses = Warehouse.objects.all()
    context = { 'inventory': inventory, 'entries': inventory, 'warehouses': warehouses}
    
    if request.method == 'GET':
        return render(request, 'inventory/edit_inventory.html', context)
    
    if request.method == 'POST':
        value = request.POST.get('value')
        item = request.POST.get('item')
        date = request.POST.get('date')
        warehouse = request.POST.get('warehouse')
        
        if None or not (value and item and date and warehouse):
            messages.error(request, "Please fill in all fields :)")
            return render(request, 'inventory/edit_inventory.html', context)
        
        # Updating inventory item in the Postgres DB 
        inventory.value = value
        inventory.date = date
        inventory.warehouse = warehouse
        inventory.item = item
        
        # Saving the new inventory item
        inventory.save()
        messages.success(request, "Inventory item has been updated :)")
        return redirect('inventory')

# Logic to delete an inventory item
def delete_inventory(request, id):
    inventory = Inventory.objects.get(pk = id) # Obtain the particular inventory to be deleted
    inventory.delete()
    messages.success(request, "Inventory item has been deleted :(")
    return redirect("inventory")
        
        