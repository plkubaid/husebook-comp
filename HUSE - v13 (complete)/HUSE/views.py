from django.shortcuts import redirect,render
from django.http import HttpResponse


def turnpage(request):
    return render(request,'mainpage.html')


def test(request):
    if request.method=='POST':
        print(request.POST)
        return HttpResponse('test')
    return render(request,'test.html')
