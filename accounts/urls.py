from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.accountpage,name ='homepage'),
    url(r'signup/$', views.createAcc,name = 'signup'),
    url(r'login/$', views.loginview, name = 'login'),
    url(r'profile/$', views.profile_info,name = 'profile'),
    url(r'logout/$', views.logout_view, name ='logout'),
    url(r'profile/edit/$',views.profile_edit, name ='profile_edit'),
    url(r'verify/$',views.verify_view, name = 'verify'),
    url(r'resend/$',views.resend_code, name = 'resend'),
    url(r'terms-conditions/$',views.terms, name='terms')
]
