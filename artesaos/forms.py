from django import forms
from .models import Artesao


class ArtesaoForm(forms.ModelForm):
    class Meta:
        model = Artesao
        fields = [
            'nome',
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
        }