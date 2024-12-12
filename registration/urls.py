from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signup,name='signup'),
    path('login/',views.Login,name='login'),
    path('home/',views.hompage, name='home'),
    path('logout/',views.Logout, name='logout'),
]
