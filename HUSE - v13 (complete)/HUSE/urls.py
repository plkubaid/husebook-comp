from django.contrib import admin
from django.conf.urls import url,include
from django.shortcuts import redirect
from. import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings





urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', views.turnpage),
    url(r'^inventory/',include('inventory.urls')),
    url(r'^accounting/',include('accounting.urls')),
    url(r'^billing/',include('billing.urls')),
    url(r'expense/',include('expense.urls')),
    url(r'^support/',include('support.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
