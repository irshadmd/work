from django.conf.urls import url
from authenticate import views
# SET THE NAMESPACE!
app_name = 'authenticate'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register',views.register,name='register'),
    url(r'^login',views.user_login,name='user_login'),
    url(r'operator_window',views.window),
    url(r'logout',views.logout),
    url(r'windowsubmit',views.windowsubmit),
    url(r'operatorskillmatrix',views.operatorskillmatrix),
]
