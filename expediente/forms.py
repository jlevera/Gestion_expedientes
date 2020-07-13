from django import forms

from .models import Carpeta

class PostForm(forms.ModelForm):

    class Meta:
        model = Carpeta
        fields = ('caratula',  'nro_expediente','año', 'secretaria', 'Providencia_de_autos_firme')