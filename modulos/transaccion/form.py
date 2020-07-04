from django import forms
from modulos.transaccion.models import Archivo


class UploadDocumentForm(forms.ModelForm):

    class Meta:
        model = Archivo
        fields = ['name', ]








