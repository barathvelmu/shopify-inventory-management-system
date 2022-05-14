from django.shortcuts import render, redirect
from inventory.models import Warehouse
from django.contrib import messages
from django.core.paginator import Paginator

# Base concept follows Views.py from the Inventory Django App. Therefore, comments will be limited on this file.

# Warehouse List Page
def index(request):
    warehouses = Warehouse.objects.all()
    
    # Pagination
    paginator = Paginator(warehouses, 10)
    page_number = request.GET.get('page')
    page_objects = Paginator.get_page(paginator, page_number)
    # Return
    context = { 'warehouses': warehouses, 'page_objects': page_objects}
    return render(request, 'warehouse/index.html', context)


# Logic to add a warehouse
def add_warehouse(request):
    warehouses = Warehouse.objects.all() 
    context= { 'warehouses':warehouses, 'entries': request.POST } 
    
    if request.method == 'GET':
        return render(request, 'warehouse/add_warehouse.html', context)
    
    if request.method == 'POST':
        # Getting the warehouse name (only entry)
        name = request.POST.get('name')
        
        # Validate if user has filled in a warehouse name
        if None or not (name):
            messages.error(request, "Please fill in the name")
            return render(request, 'warehouse/add_warehouse.html', context)
    
    # If all is well, save new warehouse to the database  
    Warehouse.objects.create(name = name)
    messages.success(request, "New warehouse has been added :)")
    return redirect('warehouse')


# Logic to edit a warehouse
def edit_warehouse(request, id):
    warehouse = Warehouse.objects.get(pk=id) 
    context = { 'warehouse': warehouse, 'entries': warehouse}
    
    if request.method == 'GET':
        # obtaining the partiular entry to edit
        return render(request, 'warehouse/edit_warehouse.html', context)
    
    if request.method == 'POST':
        name = request.POST.get('name')        
        if None or not (name):
            messages.error(request, "Please fill in the name")
            return render(request, 'warehouse/edit_warehouse.html', context)
        
        # Updating warehouse in the Postgres DB 
        warehouse.name = name
        
        # Saving the warehouse
        warehouse.save()
        messages.success(request, "Warehouse has been updated :)")
        return redirect('warehouse')


# Logic to delete a warehouse
def delete_warehouse(request, id):
    warehouse = Warehouse.objects.get(pk = id)
    warehouse.delete()
    messages.success(request, "Warehouse has been deleted :(")
    return redirect("warehouse")