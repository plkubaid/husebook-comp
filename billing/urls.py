from django.conf.urls import url
from . import views


app_name = 'billing'

urlpatterns=[
   url(r'^$',views.homepage,name='homepage'),
   url(r'invoice/$',views.invoice,name='invoice'),
   url(r'invoice/records/$',views.invoice_record, name = 'records'),
   url(r'invoice/duplicate/$',views.dup_view, name ='duplicate_invoice'),
]
