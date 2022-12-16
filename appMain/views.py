from django.shortcuts import render
from .models import Tarefas

def base(request):
    return render(request, 'base.html')
    
def home(request): 
    return render(request, 'home.html')

def tarefas(request): 
    return render(request, 'tarefas.html')

def videos(request): 
    tarefas = Tarefas.objects.all()
    return render(request,'videos.html',{'tarefas':tarefas})
 
def games(request): 
    tarefas = Tarefas.objects.all()
    return render(request,'games.html',{'tarefas':tarefas})

def atividades(request): 
    tarefas = Tarefas.objects.all()
    return render(request,'atividades.html',{'tarefas':tarefas})

def equipe(request): 
    return render(request,'equipe.html')

def sobre(request): 
    return render(request,'about_us.html')
