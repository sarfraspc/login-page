from django.urls import path
from . import views

urlpatterns = [
    path('', views.Indexpage, name='index'),
    path('login/', views.Loginpage, name='login'),
    path('home/', views.Homepage, name='home'),
    path('logout/', views.Logoutpage, name='logout'),
]