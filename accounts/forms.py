from django import forms

from django.contrib.auth import get_user_model
User = get_user_model()

class AccountsSignupForm(forms.ModelForm):
    password = forms.CharField(
                        label="Senha",
                        max_length=50,
                        widget=forms.widgets.PasswordInput()
                        )
                        
    class Meta:
        model = User
        fields = ('username', 'email', 'data_nascimento', 'cpf', 'password', )
        widgets = {
        'data_nascimento': forms.widgets.DateInput(
            attrs={'type': 'date', 'required': 'required'})
        }
