from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control', 'id': 'inputGroupFile02'}))
