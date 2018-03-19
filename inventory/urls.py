from django.conf.urls import url
from . import views

app_name='inventory'


urlpatterns =[
     url(r'^$',views.inventory,name='homepage'),
     url(r'list/$',views.inventory_list,name='list'),
     url(r'add/$',views.inventory_add, name = 'add'),
     url(r'update/$',views.inventory_update,name='update'),
]
