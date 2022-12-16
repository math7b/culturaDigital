from appMain import views
from django.urls import path
from django.views.generic import TemplateView
from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.home, name='dashboard'),
    path('tarefas/', views.tarefas, name='tarefas'),
    path('videos/', views.videos, name='videos'),
    path('games/', views.games, name='games'),
    path('atividades/', views.atividades, name='atividades'),
]
if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  