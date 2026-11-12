
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import Artesao


class ArtesaoForm(forms.ModelForm):

    email = forms.EmailField(
        label='E-mail',
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Digite seu e-mail',
            'autocomplete': 'email'
        })
    )

    senha = forms.CharField(
        label='Senha',
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Crie uma senha',
            'autocomplete': 'new-password'
        })
    )

    class Meta:
        model = Artesao

        fields = [
            'nome',
            'email',
            'senha',
            'nome_loja',
            'estado',
            'cidade',
            'regiao',
            'descricao',
            'telefone',
            'instagram',
        ]

        labels = {
            'nome': 'Nome do artesão',
            'nome_loja': 'Nome da loja',
            'estado': 'Estado',
            'cidade': 'Cidade',
            'regiao': 'Região',
            'descricao': 'Descrição da loja',
            'telefone': 'WhatsApp/Telefone',
            'instagram': 'Instagram',
        }

        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'telefone': forms.TextInput(attrs={
                'placeholder': '(00) 00000-0000',
                'maxlength': '15',
                'id': 'telefone'
            }),
        }

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                'Este e-mail já está cadastrado.'
            )

        return email

    def clean_senha(self):
        senha = self.cleaned_data['senha']
        validate_password(senha)
        return senha
