from django import forms
from .models import UploaderFile

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploaderFile
        fields = ['file']