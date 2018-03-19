from django.conf.urls import url
from. import views

app_name='accounting'

urlpatterns = [
    url(r'^$',views.dashboard, name = 'dashboard'),
    url(r'calculations/$',views.calculations, name = 'calc'),
    url(r'detail/(?P<date>[\w-]+)/$',views.detail, name = 'detail')
]
