from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('accounts/login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]