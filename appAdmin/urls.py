from appAdmin import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='dashboard'),
    path('jogos/', views.jogos, name='jogos'),
    path('jogos/pendentes/', views.jogospendentes, name='jogospendentes'),
    path('videos/', views.videos, name='videos'),
    path('videos/pendentes/', views.videospendentes, name='videospendentes'),
    path('atividades/', views.atividades, name='atividades'),
    path('atividades/pendentes/', views.atividadespendentes, name='atividadespendentes'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.deletarTarefa, name='deletarTarefa'),
    path('publicar/<int:id>/', views.publicar, name='publicar'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('usuarios/<int:id>/delete', views.deletarUsuario, name='deleteUser'),
    path('usuarios/<int:id>/profile', views.profile, name='profile'),
]