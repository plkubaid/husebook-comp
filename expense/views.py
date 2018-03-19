from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from. import models as m
from accounting import models as am

# Create your views here.


@login_required
def record(request):
    data = am.TranRecord.objects.filter(user = request.user,category='Expense').order_by('-date')
    return render(request,'expense/record.html',{'data':data})


@login_required
def homepage(request):
    return render(request,'expense/homepage.html')

@login_required
def exp(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        cost = request.POST.get('cost')
        price = 0
        user = request.user
        #saving to acc for calculations
        a_data = am.AccountsInvoice()
        a_data.t_id = name
        a_data.price = price
        a_data.cost = float(cost)
        a_data.user = user
        # saving to accounting record
        a_data2 = am.TranRecord()
        a_data2.name = name
        a_data2.cost = float(cost)
        a_data2.price = price
        a_data2.user = user
        a_data2.category = 'Expense'
        a_data2.buyer = 'Our Company'
        a_data2.profit = -float(cost)
        a_data2.save()
        a_data.save()
        return redirect('/accounting/')
    return render(request,'expense/ir_exp.html')
