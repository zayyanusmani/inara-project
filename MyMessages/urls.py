from django.urls import path
from . import views

app_name = 'messages'
urlpatterns = [
    path('', views.home, name='home'),    
    path('create-user', views.createUser, name='create_user'), 
    path('send-message', views.sendMessage, name='send_message'),
    path('stats', views.stats, name='stats')    
        
]