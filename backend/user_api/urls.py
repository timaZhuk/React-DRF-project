from django.urls import path
from . import views

urlpatterns = [
    path('registers', views.UserRegister.as_view(), name='registers'),
    path('login',views.UserLogin.as_view(),name='login'),
    path('logout',views.UserLogout.as_view(),name='logout'),
    path('user',views.UserView.as_view(),name='user')

]
