from django.utils.translation import gettext_lazy as _
from django import forms
from appMain.models import Tarefas
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group,User


class UserProfileForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'password1', 'password2', 'group']

class AddTarefas(forms.ModelForm):
    class Meta:
        model = Tarefas
        fields = ['nome', 'link', 'descricao', 'materia', 'categoria','publicado','imagem' ]

    
        