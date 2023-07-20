from django import forms
from .models import Producto, Bodegas, Autores, Editoriales

class ProductoForms(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class BodegasForms(forms.ModelForm):
    class Meta:
        model = Bodegas
        fields = '__all__'

class AutoresForms(forms.ModelForm):
    class Meta:
        model = Autores
        fields = '__all__'

class EditorialesForms(forms.ModelForm):
    class Meta:
        model = Editoriales
        fields = '__all__'