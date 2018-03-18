from django.conf.urls import url
from . import views


app_name= 'support'

urlpatterns = [
    url(r'open-support/$',views.unknown,name='unknown'),
    url(r'customer-support/$', views.customer_support, name= 'customer-support'),
    url(r'suggestion/$',views.suggestion,name='suggestion'),
    url(r'emp/panel/$',views.support_panel,name='support-panel'),
    url(r'emp/panel/opens/$',views.openseen,name = 'oseen'),
    url(r'emp/panel/openu/$',views.openunseen,name = 'ounseen'),
    url(r'emp/panel/customers/$',views.customerseen,name = 'cseen'),
    url(r'emp/panel/customeru/$',views.customerunseen,name = 'cunseen'),
    url(r'emp/panel/suggests/$',views.suggestseen,name = 'sseen'),
    url(r'emp/panel/suggestu/$',views.suggestunseen,name = 'sunseen'),
    url(r'support/detail/(?P<id>[0-9]+)/(?P<typo>[\w]+)/',views.detail,name = 'sdetail')
]
