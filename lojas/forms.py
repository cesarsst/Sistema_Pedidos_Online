from django import forms

class ComentarioLoja(forms.Form):

    nome = forms.CharField(label='Nome', max_length=200)
    email = forms.EmailField(label='E-mail')
    mensagem = forms.CharField(label='Mensagem/Duvida', widget=forms.Textarea)


