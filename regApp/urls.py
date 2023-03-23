from django.urls import path 
from .views import *
urlpatterns = [
    path('reg/',registerPage,name='register'),
    path('navToLogin/',navigateToLoginPage,name='navToLogin'),
    path('signup/',signup,name='signup'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout')
]