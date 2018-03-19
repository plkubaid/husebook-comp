from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from inventory.models import Inventory
from.models import Invoice,TempTran,InvoiceRecord
from django.db.models import Q
from accounts.models import Profile
from z.models import AccountsInvoice,TranRecord
import string
import random


@login_required
def homepage(request):
    return render(request,'billing/homepage.html')

@login_required
def invoice(request):
    if request.method == 'POST':
        print(request.POST)
        buyer = request.POST.get('buyer')
        codeall = request.POST.getlist('code')
        priceall = request.POST.getlist('price')
        quanall = request.POST.getlist('quantity')
        t_id = g(12)
        price_total=0
        cost_total = 0
        if len(codeall)==len(priceall) and len(priceall)==len(quanall):
            for i in range(len(codeall)):
                name = codeall[i]
                unprice = priceall[i]
                quan = quanall[i]
                price = int(unprice)*int(quan)
                if request.POST.get('sersale'):
                    cost = 0
                    profit = price
                    category = 'Services'
                elif request.POST.get('invsale'):
                    category = 'Inventory Sales'
                    inv_d = Inventory.objects.filter(Q(user=request.user,name=name)|Q(user=request.user,code=name))
                    if inv_d:
                        if inv_d[0].quantity > int(quan):
                            inv_d[0].quantity = inv_d[0].quantity-int(quan)
                            inv_d[0].price = inv_d[0].price-inv_d[0].unit_price*int(quan)
                            inv_d[0].save()
                            cost=inv_d[0].unit_price*int(quan)
                            profit = price-cost
                            name = inv_d[0].name
                        else:
                            message= 'Quantity of some goods are low than required.'
                            return render(request,'billing/homepage.html',{'message':message})
                    else:
                        message='your code no.'+str(i+1)+' not found in inventory!'
                        return render(request,'billing/homepage.html',{'message':message})
                else:
                    message='There was an issue try again or contact support!'
                    return render(request,'billing/homepage.html',{'message':message})
                #saving to invoice_record
                print(profit)
                mod = Invoice()
                mod.transaction_id = t_id
                mod.name = name
                mod.quantity = quan
                mod.user = request.user
                mod.price = price
                mod.unit_price = unprice
                mod.buyer = buyer
                mod.save()
                #saving to transaction records
                tr = TranRecord()
                tr.name = name
                tr.price = price
                tr.cost = cost
                tr.buyer = buyer
                tr.profit = profit
                tr.category = category
                tr.user = request.user
                price_total = price_total+price
                cost_total = cost_total+cost
                tr.save()
            #saving for invoice records
            recordup = InvoiceRecord()
            recordup.transaction_id = t_id
            recordup.user = request.user
            recordup.buyer = buyer
            recordup.price = price
            recordup.save()
            #saving for account calculations
            ai = AccountsInvoice()
            ai.t_id = t_id
            ai.user = request.user
            ai.price = price_total
            ai.cost = cost_total
            ai.save()
            finalinfo = Invoice.objects.filter(transaction_id=t_id,user = request.user)
            #print(finalinfo)
            data = Profile.objects.get(username = request.user)
            return render(request,'billing/invoice.html',{'final':finalinfo,'data':data,"price":price_total,'buyer':buyer})
        message = 'There was an issue!'
        return redirect(request,'billing/homepage.html',{'message':message})#render(request,'billing/invoice.html',{'final':finalinfo,'data':data,"price":price_total})
    return redirect('/billing/')


def g(size):
    a = ''
    for x in range(size):
        a = a+ str(random.choice(string.ascii_uppercase)+str(random.randint(1,9)))
    return(a)

@login_required
def invoice_record(request):
    data = InvoiceRecord.objects.filter(user = request.user).order_by('-date')
    #print(data)
    return render(request,'billing/records.html',{'data':data})


#def delete_all(request):
#    Invoice.objects.all().delete()
#    InvoiceRecord.objects.all().delete()
#    return HttpResponse('done')

@login_required
def dup_view(request):
    if request.method == 'POST':
        #print(request.POST)
        t_id = request.POST.get('t_id')
        finalinfo = Invoice.objects.filter(transaction_id=t_id,user = request.user)
        #print(finalinfo)
        pric = InvoiceRecord.objects.get(transaction_id=t_id)
        price = pric.price
        buyer = pric.buyer
        data = Profile.objects.get(username = request.user)
        return render(request,'billing/invoice.html',{'final':finalinfo,'data':data,'price':price,'buyer':buyer})
    return render(request,'billing/invoice.html')
