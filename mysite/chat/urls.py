from django.urls import path
from . import views

app_name = "chat"
urlpatterns = [    
    path('', views.home, name='home'),
    path('<str:room_name>/<str:username>/', views.room, name='room'),
    path('checkview', views.checkview, name='check'),
]
