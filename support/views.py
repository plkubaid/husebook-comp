from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import support,Open_Support,suggestionM,support_employee
from accounts.models import Profile
from.forms import OpenSupport,CustomerSupport,Suggestion
import random
# Create your views here.
@login_required
def detail(request,id,typo):
    if typo=='customer':
        data = support.objects.get(pk=id)
        data.seen=True
        data.save()
        return render(request,'support/support_data.html',{'data':data})
    elif typo=='suggest':
        data = suggestionM.objects.get(pk=id)
        data.seen=True
        data.save()
        return render(request,'support/support_data.html',{'data':data})
    elif typo=='open':
        data = Open_Support.objects.get(pk=id)
        data.seen = True
        data.save()
        return render(request,'support/support_data.html',{'data':data})
    return HttpResponse(id)

@login_required
def customer_support(request):
    data = Profile.objects.get(username=request.user)
    if request.method =='POST':
        email = data.email
        body = request.POST.get('body')
        com_type = 'Customer'
        com_id = g(7)
        form = support()
        form.complain_id = com_id
        form.email = email
        form.body = body
        form.com_type = com_type
        form.user = request.user
        form.save()
        message = 'Your support query has been saved complain_id:'+str(com_id)+' you will be contacted through your email.'
        return render(request,'support/customer_support.html',{'message':message})
    form = CustomerSupport()
    return render(request,'support/customer_support.html',{'form':form,'data':data})

@login_required
def suggestion(request):
    data = Profile.objects.get(username=request.user)
    if request.method=='POST':
        form = suggestionM()
        form.email = data.email
        form.body = request.POST.get('body')
        form.user = request.user
        form.save()
        message = 'Your suggestion has been saved, THANK YOU!'
        return render(request,'support/suggestion.html',{'message':message})
    form = Suggestion()
    return render(request,'support/suggestion.html',{'form':form,'data':data})


def unknown(request):
    if request.method == 'POST':
        form = OpenSupport(request.POST)
        com_type ='Unknown'
        com_id = g(7)
        email = request.POST.get('email')
        body = request.POST.get('body')
        model =  Open_Support()
        model.complain_id = com_id
        model.com_type = com_type
        model.email = email
        model.body = body
        model.save()
        print('save')
        return redirect('/')
    form = OpenSupport()
    return render(request,'support/open_support.html',{'form':form})

@login_required
def support_panel(request):
    data = support_employee.objects.filter(user=request.user)
    if data:
        cu = support.objects.filter(seen=False)
        ou = Open_Support.objects.filter(seen=False)
        su = suggestionM.objects.filter(seen=False)
        return render(request,'support/support_panel.html',{'cu':len(cu),'ou':len(ou),'su':len(su)})
    return redirect('/')

@login_required
def openseen(request):
    dat = support_employee.objects.filter(user=request.user)
    if dat:
        data = Open_Support.objects.filter(seen=False).order_by('date')
        typp = 'open'
        sub = 'seen'
        return render(request,'support/support_detail.html',{'data':data,'tyyp':typp,'sub':sub})
    return redirect('/')

@login_required
def openunseen(request):
    dat = support_employee.objects.filter(user=request.user)
    if dat:
        data = Open_Support.objects.filter(seen=True).order_by('-date')
        typp = 'open'
        sub = 'seen'
        return render(request,'support/support_detail.html',{'data':data,'tyyp':typp,'sub':sub})
    return redirect('/')

@login_required
def customerseen(request):
    dat = support_employee.objects.filter(user=request.user)
    if dat:
        data = support.objects.filter(seen=True).order_by('-date')
        typp = 'customer'
        sub = 'seen'
        return render(request,'support/support_detail.html',{'data':data,'tyyp':typp,'sub':sub})
    return redirect('/')

@login_required
def customerunseen(request):
    dat = support_employee.objects.filter(user=request.user)
    if dat:
        data = support.objects.filter(seen=False).order_by('-date')
        typp = 'customer'
        sub = 'unseen'
        return render(request,'support/support_detail.html',{'data':data,'tyyp':typp,'sub':sub})
    return redirect('/')

@login_required
def suggestunseen(request):
    dat = support_employee.objects.filter(user=request.user)
    if dat:
        data = suggestionM.objects.filter(seen=False).order_by('-date')
        typp = 'suggest'
        sub = 'unseen'
        return render(request,'support/support_detail.html',{'data':data,'tyyp':typp,'sub':sub})
    return redirect('/')

@login_required
def suggestseen(request):
    dat = support_employee.objects.filter(user=request.user)
    if dat:
        data = suggestionM.objects.filter(seen=True).order_by('-date')
        typp = 'suggest'
        sub = 'seen'
        return render(request,'support/support_detail.html',{'data':data,'tyyp':typp,'sub':sub})
    return redirect('/')

def g(size):
    a = ''
    for x in range(size):
        a = a+str(random.randint(1,9))
    return(a)
