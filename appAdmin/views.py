from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from appMain.models import Tarefas
from .forms import AddTarefas, UserProfileForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


@login_required(login_url='/accounts/login/')
def home(request):
    tarefas =  Tarefas.objects.filter(publicado=True).count()
    context = {'tarefas':tarefas}
    return render(request, 'home_admin.html', context)

@login_required(login_url='/accounts/login/')
def jogos(request):
    tarefas = Tarefas.objects.all()
    form = AddTarefas()
    if request.method == 'POST' :
        form = AddTarefas(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            form.save()
            return redirect('/dashboard/jogos/')

    context = {'tarefas':tarefas, 'form':form}
    return render(request,'repojogos.html', context)

@login_required(login_url='/accounts/login/')
def jogospendentes(request):
    tarefas = Tarefas.objects.all()
    form = AddTarefas()

    if request.method == 'POST' :
        form = AddTarefas(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            form.save()
            return redirect('/dashboard/jogos/pendentes')

    context = {'tarefas':tarefas, 'form':form}
    return render(request,'jogos_pendentes.html', context)

@login_required(login_url='/accounts/login/')
def videos(request):
    tarefas = Tarefas.objects.all()
    form = AddTarefas()
    if request.method == 'POST' :
        form = AddTarefas(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            form.save()
            return redirect('/dashboard/videos/')

    context = {'tarefas':tarefas, 'form':form}
    return render(request,'repovideos.html', context)

@login_required(login_url='/accounts/login/')
def videospendentes(request):
    tarefas = Tarefas.objects.all()
    form = AddTarefas()
    if request.method == 'POST' :
        form = AddTarefas(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            form.save()
            return redirect('/dashboard/videos/pendentes')

    context = {'tarefas':tarefas, 'form':form}
    return render(request,'videos_pendentes.html', context)

@login_required(login_url='/accounts/login/')
def atividades(request):
    tarefas = Tarefas.objects.all()
    form = AddTarefas()
    if request.method == 'POST' :
        form = AddTarefas(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            form.save()
            return redirect('/dashboard/atividades')

    context = {'tarefas':tarefas, 'form':form}
    return render(request,'repoativ.html', context)

@login_required(login_url='/accounts/login/')
def atividadespendentes(request):
    tarefas = Tarefas.objects.all()
    form = AddTarefas()
    if request.method == 'POST' :
        form = AddTarefas(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.usuario = request.user
            form.save()
            return redirect('/dashboard/atividades/pendentes')

    context = {'tarefas':tarefas, 'form':form}
    return render(request,'atividades_pendentes.html', context)

@login_required(login_url='/accounts/login/')
def edit(request, id):
    tarefas = Tarefas.objects.get(id = id)

    form = AddTarefas(request.POST or None,request.FILES or None, instance=tarefas)
    if form.is_valid():
        form.save()
        return redirect('/dashboard/jogos/')
    
    context = {'tarefas':tarefas, 'form':form}
    return render(request, 'edit.html', context)

@login_required(login_url='/accounts/login/')
def deletarTarefa(request, id):
    tarefas = Tarefas.objects.get(id=id)
    tarefas.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/accounts/login/')
def publicar(request, id):
    tarefas = Tarefas.objects.get(id=id)
    tarefas.publicado = True 
    tarefas.save()   
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/accounts/login/')
def usuarios(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']        
            group.user_set.add(user)
            
    else:
        form = UserProfileForm()       

    users = User.objects.all()
    context = {'users':users,'form':form}
    return render(request, 'usuarios.html', context)


def profile(request, id):
    getUser = User.objects.get(id = id)
    countUser_tarefas = Tarefas.objects.filter(usuario=getUser).count()
    countUser_tarefaspublicadas = Tarefas.objects.filter(usuario=getUser, publicado=True).count()
    tarefas = Tarefas.objects.filter(usuario=getUser)

    form = SetPasswordForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('/dashboard/usuarios/')

    context = {'tarefas':tarefas,'getUser':getUser,'form':form,'countUser_tarefas':countUser_tarefas,'countUser_tarefaspublicadas':countUser_tarefaspublicadas}
    return render(request, 'profile.html', context)


def deletarUsuario(request, id):
    deleteUser = User.objects.get(id = id)
    deleteUser.delete()
    return redirect('/dashboard/usuarios')