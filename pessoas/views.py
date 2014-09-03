from django.shortcuts import render, HttpResponseRedirect
from pessoas.forms import PessoaForm, LoginForm
from django.contrib.auth import authenticate, logout, login as meu_login
from django.contrib.auth.decorators import login_required

def index(request):
		return render(request, 'index.html')

def login(request):
		form = LoginForm()
		return render(request, 'login.html', {'form':form})

# Create your views here.
