from django import forms
from ckeditor.widgets import CKEditorWidget

class PagesCreate(forms.Form):

     titulo = forms.CharField(max_length=120, label="Título")
     subtitulo = forms.CharField(max_length=500, label="Subtítulo")
     texto = forms.CharField(widget=CKEditorWidget())
     imagen = forms.ImageField(required=False)

class PagesUpdate(forms.Form):

     titulo = forms.CharField(max_length=120, label="Título")
     subtitulo = forms.CharField(max_length=500, label="Subtítulo")
     texto = forms.CharField(widget=CKEditorWidget())
     imagen = forms.ImageField(required=False)