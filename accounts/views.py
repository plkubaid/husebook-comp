from django.shortcuts import render,redirect
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import smtplib
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from .models import Profile,verified
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import Pform,CustomForm


def accountpage(request):
    return render(request,'accounts/homepage.html')

def g(size):
    a = ''
    for x in range(size):
        a = a+str(random.randint(1,9))
    return(a)

def createAcc(request):
    if request.method == 'POST':
        #print(request.POST)
        if request.POST.get('agr-check'):
            form = UserCreationForm(data=request.POST)
            if form.is_valid():
                password = request.POST.get('password1')
                dx_ball = Profile.objects.filter(email=request.POST.get('email'))
                if dx_ball:
                    message = 'An account with this email exists\nTry logging in'
                    return render(request,'accounts/login.html',{'message':message})
                #User.objects.get(username=user)
                user = form.save()
                email = request.POST.get('email')
                info = Profile()
                info.username=user
                info.email = email
                info.first_name = request.POST.get('first_name')
                info.last_name = request.POST.get('last_name')
                info.business = request.POST.get('business')
                info.save()
                v_key = g(5)
                ver = verified()
                ver.user = user
                ver.v_key = v_key
                ver.is_verified = False
                ver.save()
                verify_mail(email,v_key)
                return render(request,'accounts/verify.html',{'user':user,'pass':password})
            return redirect('/accounts/signup/')
        return render(request,'accounts/signup.html',{'message':'Terms Not accepted!'})
    form = CustomForm()
    return render(request, 'accounts/signup.html',{'form':form})

def loginview(request):
    if request.method == 'POST':
        #print(request.POST)
        form = AuthenticationForm(data=request.POST)
        if form.is_valid:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    ver = verified.objects.get(user=user)
                    if ver.is_verified:
                        #print(user)
                        login(request,user)
                        if request.POST.get('next'):
                            return redirect(request.POST.get('next'))
                        return redirect('/accounts/profile/')
                    return render(request,'accounts/verify.html',{'user':user,'pass':password})
                message = 'your account is de-activated! (contact support)'
                return render(request,'accounts/message.html')
    form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def profile_info(request):
    data = request.user
    x = User.objects.get(username=data)
    user = x.id
    datas = Profile.objects.get(username=user)
    return render(request,'accounts/profile.html',{'data':datas,'user':data})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        print(request.POST)
        dx_ball = Profile.objects.get(username=request.user)
        #dx_ball.delete()
        if request.FILES:
            form = Pform(request.POST,request.FILES)
            if form.is_valid:
                if dx_ball.profile_picture.name != 'default.png':
                    dx_ball.rem_file()
                dx_ball.delete()
                ins = form.save(commit=False)
                ins.username=request.user
                ins.save()
                return redirect('/accounts/profile/')
            #print(form)
            else:
                return redirect("/accounts/profile/edit/")
        else:
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')
            business = request.POST.get('business')
            dx_ball.first_name = fname
            dx_ball.last_name = lname
            dx_ball.business = business
            dx_ball.save()
            return redirect('/accounts/profile/')
    else:
        form = Pform()
        data = Profile.objects.get(username=request.user)
        return render(request,'accounts/profile_edit.html',{'form':form,'data':data})

def verify_view(request):
        if request.method == 'POST':
            if request.POST.get('user'):
                username = request.POST.get('user')
                password = request.POST.get('pass')
                u = User.objects.get(username=username)
                data = verified.objects.filter(user=u.id)
                print
                if data:
                    if data[0].is_verified:
                        login(request,username)
                        return redirect('/accounts/profile/')
                    else:
                        code = request.POST.get('email_verify')
                        print(code)
                        code2 = data[0].v_key
                        print(code2)
                        if int(code) == int(code2):
                            data[0].is_verified = True
                            data[0].save()
                            print(username)
                            print(password)
                            user = authenticate(username=username,password=password)
                            print(user)
                            if user is not None:
                                login(request,user)
                            return redirect('/accounts/profile/')
                        return render(request,'accounts/verify.html',{'user':username,'pass':password,'message':'code does not match!'})
                return redirect('/accounts/signup/')
            return redirect('/accounts/signup/')
        return render(request,'accounts/verify.html')

def verify_mail(to,code):
    data = "<h2>your verification code is:</h2><br><h1>"+str(code)+"</h1>"
    message = MIMEMultipart()
    message['To'] = to
    message['From'] = 'Huse Books'
    message['subject'] = 'Verification'
    html_body = MIMEText(data,'html')
    message.attach(html_body)

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('husebooks@gmail.com','humairashahid')
    server.sendmail('husebooks@gmail.com',to,
                    message.as_string())
    server.quit()

def resend_code(request):
    code = g(5)
    if request.method == 'POST':
        user = request.POST.get('userr')
        d1 = User.objects.get(username=user)
        password = request.POST.get('passr')
        data = Profile.objects.get(username=d1.id)
        ver = verified.objects.get(user=d1.id)
        ver.v_key = code
        ver.save()
        email = data.email
        print(email)
        verify_mail(email,code)
        return render(request,'accounts/verify.html',{'user':user,'pass':password})
    return redirect('accouns:login')

def terms(request):
    return render(request,'accounts/terms.html')
