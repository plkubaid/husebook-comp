from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import AccountsInvoice,Accounting,TranRecord
from accounts.models import Profile
from django.db.models import Q
import datetime
from django.contrib.auth.decorators import login_required

@login_required
def calculations(request):
    date_today = datetime.date.today().isoformat()
    cost_total = 0
    price_total = 0
    data = AccountsInvoice.objects.filter(user=request.user)
    data1 = Accounting.objects.filter(user=request.user,date=date_today)
    if data:
        for point in data:
            cost_total = cost_total+point.cost
            price_total = price_total+point.price
            profit = price_total-cost_total
        if data1:
            info_up = Accounting.objects.get(user=request.user,date=date_today)
            profit = profit+info_up.profit
        else:
            info_up = Accounting()
            info_up.user = request.user
        info_up.profit = profit
        if profit>0:
            info_up.status = True
        else:
            info_up.status = False
        info_up.save()
        AccountsInvoice.objects.filter(user=request.user).delete()
        return redirect('/accounting/')
    return redirect('/accounting/')

@login_required
def dashboard(request):
    data1 = AccountsInvoice.objects.filter(user = request.user)
    if data1:
        return redirect('/accounting/calculations/')
    data = Accounting.objects.filter(user = request.user).order_by('-date')[:10]
    if data:
        b_info = Profile.objects.get(username = request.user)
        return render(request,'accounting/dashboard.html',{'data':data,'b_info':b_info})
    return render(request,'accounting/dashboard.html')

@login_required
def detail(request,date):
    data1 = AccountsInvoice.objects.filter(user = request.user)
    if data1:
        return redirect('/accounting/calculations/')
    data = TranRecord.objects.filter(date=date,user = request.user)
    if data:
        return render(request,'accounting/detail.html',{'data':data})
    return HttpResponse('NO DETAILS')
