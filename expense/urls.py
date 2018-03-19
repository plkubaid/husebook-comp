from django.conf.urls import url
from . import views

app_name = 'expense'

urlpatterns=[
     url(r'^$',views.homepage,name = 'homepage'),
     url(r'^record/$',views.record,name = 'record'),
     url(r'^normal/$',views.exp,name = 'irexp'),
]
