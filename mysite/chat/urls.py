from django.urls import path
from . import views

app_name= 'chat'
urlpatterns = [
    path('messages/', views.message_list, name='message_list'),
    path('messages/<int:pk>/', views.message_detail, name='message_detail'),
    path('', views.chat_view, name='chat'),
]