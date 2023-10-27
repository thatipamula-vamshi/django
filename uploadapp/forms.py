from django import forms 
from uploadapp.models import uploads, uploadfile

class UploadForm(forms.ModelForm):
    class Meta:
        model = uploads
        fields ='__all__'
    
class UploadFile(forms.ModelForm):
    class Meta:
        model = uploadfile
        fields ='__all__'
    