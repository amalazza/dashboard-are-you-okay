from django import forms


from .models import Pertanyaan

class PertanyaanModelForm(forms.ModelForm):
    pertanyaan = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Pertanyaan",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Pertanyaan
        fields = [
            'pertanyaan'
        ]
