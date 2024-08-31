from django import forms
from Gallery.models import Gallery

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields ='__all__'