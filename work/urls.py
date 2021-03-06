from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from authenticate import views
from authenticate import urls
from attendence import views
from attendence import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^authenticate/',include('authenticate.urls')),
    url(r'^attendence/',include('attendence.urls')),
    path('operators/',include('operators.urls')),
]
