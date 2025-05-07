from django import forms                          
from sistema.models import Filme                

class FilmeForm(forms.ModelForm):    
    class Meta:           
        model = Filme                               
        fields = ['nome_do_filme', 'ano_lancamento', 'estudio',  'sinopse']  