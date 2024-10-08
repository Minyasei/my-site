from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')), 
    path('', include('landingPage.urls')),
    path('chats/', include('chats.urls',)),
]