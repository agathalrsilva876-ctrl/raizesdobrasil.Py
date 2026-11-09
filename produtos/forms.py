
from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'imagem']

        labels = {
            'nome': 'Nome do produto',
            'descricao': 'Descrição do produto',
            'preco': 'Preço',
            'imagem': 'Imagem do produto',
        }

        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }
