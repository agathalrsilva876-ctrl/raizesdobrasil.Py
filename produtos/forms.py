from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco']

        labels = {
            'nome': 'Nome do produto',
            'descricao': 'Descrição do produto',
            'preco': 'Preço',
        }

        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }