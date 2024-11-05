from django.urls import path
from . import views


urlpatterns = [
    path('',views.signuppage,name='signupurl'),
    path('login/',views.loginpage,name='loginurl'),
    path('loginpage/',views.success,name='sucessurl')
]