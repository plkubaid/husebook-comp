from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Inventory
from django.contrib.auth.decorators import login_required
from.forms import InventoryAdd,InventoryUpdate
from django.db.models import Q


@login_required
def inventory(request):
    return render(request,'inventory/homepage.html')


@login_required
def inventory_list(request):
    data = Inventory.objects.filter(user=request.user)
    return render(request,'inventory/inventory_list.html',{'data':data})


@login_required
def inventory_add(request):
    if request.method == 'POST':
        print(request.POST)
        form = InventoryAdd(request.POST)
        if form.is_valid:
            code = request.POST.get('code')
            name = request.POST.get('name')
            data = Inventory.objects.filter(Q(code=code,user=request.user))
            if data:
                warn = 'Item with code already exists!'
                form = InventoryAdd(request.POST)
                return render(request,'inventory/inventory_add.html',{'form':form,'warn':warn})
            quantity = request.POST.get('quantity')
            price = request.POST.get('price')
            unit_price= int(price)/int(quantity)
            instance = form.save(commit=False)
            instance.user = request.user
            instance.unit_price = unit_price
            print(instance.unit_price)
            instance.save()
            return redirect('/inventory/list/')
    form = InventoryAdd()
    return render(request,'inventory/inventory_add.html',{'form':form})

@login_required
def inventory_update(request):
    if request.method=='POST':
        #print(request.POST)
        form = InventoryUpdate(request.POST)
        if form.is_valid:
            rawinfo = request.POST
            code=rawinfo['code']
            #name = rawinfo['name']
            price = rawinfo['price']
            quantity = rawinfo['quantity']
            data = Inventory.objects.filter(Q(code=code,user=request.user)|Q(name=code,user=request.user))
            if data:
                if len(data) < 2:
                    if data[0]:
                        info = data[0]
                        new_quan=int(info.quantity)+int(quantity)
                        new_price = int(price)+int(info.price)
                        new_unit_price = new_price/new_quan
                        info.quantity = new_quan
                        info.price = new_price
                        info.unit_price = new_unit_price
                        info.save()
                        return redirect("/inventory/list/")
                warn = 'Two Items Found!, correct it!'
                return render(request,'inventory/inventory_update.html',{'form':form,'warn':warn})
            warn = 'Item Not Found!'
            return render(request,'inventory/inventory_update.html',{'form':form,'warn':warn})
    else:
        form = InventoryUpdate()
        return render(request,'inventory/inventory_update.html',{'form':form})
