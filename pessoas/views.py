from django.shortcuts import render, HttpResponseRedirect
from pessoas.forms import PessoaForm, LoginForm, cadastroForm
from django.contrib.auth import authenticate, logout, login as meu_login
from django.contrib.auth.decorators import login_required
from pessoas.models import Pessoa
from django.core.mail import send_mail
	
def index(request):
		return render(request, 'index.html')

def login(request):
		form = LoginForm()
		return render(request, 'login.html', {'form':form})

def validar(request):
		if request.method == 'POST':
				form = LoginForm(request.POST)

				if form.is_valid():
						pessoa = authenticate(username=form.data['login'], password=form.data['senha'])

						if pessoa is not None:
								if pessoa.is_active:
										meu_login(request, pessoa)
										return HttpResponseRedirect('/dashboard/')
								else:
										return render(request, 'login.html', {'form':form})
						else:
								return render(request, 'login.html', {'form':form})
				else:
						return render(request, 'login.html', {'form':form})
		else:
			return HttpResponseRedirect('/login/')

def logoff(request):
		logout(request)
		return HttpResponseRedirect('/')

@login_required()
def dashboard(request):
		return render(request, 'dashboard.html')
# Create your views hereself.

def cadastro(request):
    	form = cadastroForm()
    	return render(request,'cadastro.html',{'form':form})

def cadastro_validar(request):
	    if request.method == 'POST':
	        form = cadastroForm(request.POST)

	        if form.is_valid():
	            pessoa = Pessoa(
	                username=form.data['login'], 
	                email=form.data['email'],
	                is_active=False
	            )
	            pessoa.set_password(form.data['senha'])
	            pessoa.save()
	            print('http://127.0.0.1:8000/token/'+str(pessoa.pk))
	            if send_mail('Campo assunto ', 'Valide o seu email: http://127.0.0.1:8000/cadastro_validar/token/'+str(pessoa.pk), 'roodrigoprogrammer@gmail.com',
	    [pessoa.email], fail_silently=True):
	                return render(request,'cadastro.html',{'form':form})
            	return render(request,'index.html',{'form':form})

def token(request, numero):
	    pessoa = Pessoa.objects.get(pk=numero)
	    pessoa.is_active = True
	    pessoa.save()
	    return HttpResponseRedirect('/login/')