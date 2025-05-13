from django import forms                          
from sistema.models import Filme                

class FilmeForm(forms.ModelForm):    
    class Meta:           # Meta class serve para configurar o formulário
        model = Filme                               
        fields = ['nome_do_filme', 'ano_lancamento', 'genero', 'estudio',  'sinopse']  