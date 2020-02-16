from django.conf.urls import url
from attendence import views
# SET THE NAMESPACE!
app_name = 'attendence'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^$',views.takeattendence),
    url(r'^submitattendence',views.submitattendence),
]
