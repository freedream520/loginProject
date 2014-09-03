from django import forms
from pessoas.models import Pessoa

class PessoasForm(forms.ModelForm):
		password = forms.CharField(widget=forms.PasswordInput)
		class Meta:
					model = Pessoa

class LoginForm(forms.Form):
		login = forms.CharField(max_length=100, requered=True)
		senha = forms.CharField(widget=forms.PasswordInput, requered=True)

