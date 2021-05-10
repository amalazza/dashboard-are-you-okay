from django import forms


from .models import *

class PenggunaModelForm(forms.ModelForm):
    pengguna = forms.CharField(
        widget=forms.TextInput(
            attrs={
                # "placeholder" : "Pengguna",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Pengguna
        fields = [
            'nama', 'email', 'ttl', 'jenis_kelamin', 'pekerjaan'
        ]

class PertanyaanModelForm(forms.ModelForm):
    pertanyaan = forms.CharField(
        widget=forms.TextInput(
            attrs={
                # "placeholder" : "Pertanyaan",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Pertanyaan
        fields = [
            'pertanyaan', 'bobot'
        ]

class JawabanModelForm(forms.ModelForm):
    jawaban = forms.CharField(
        widget=forms.TextInput(
            attrs={
                # "placeholder" : "Jawaban",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Jawaban
        fields = [
            'jawaban', 'bobot'
        ]

class PenangananModelForm(forms.ModelForm):
    penanganan = forms.CharField(
        widget=forms.TextInput(
            attrs={
                # "placeholder" : "Penanganan",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Penanganan
        fields = [
            'tingkatdepresi_id', 'judul', 'cover', 'isi'
        ]

class ArtikelModelForm(forms.ModelForm):
    artikel = forms.CharField(
        widget=forms.TextInput(
            attrs={
                # "placeholder" : "Artikel",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = Artikel
        fields = [
            'judul', 'cover', 'isi'
        ]