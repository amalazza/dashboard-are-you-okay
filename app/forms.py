from django import forms
from cloudinary.models import CloudinaryField



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
        fields = "__all__"

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
        fields = "__all__"

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
        fields = "__all__"

class PenangananModelForm(forms.ModelForm):
    # TingkatDepresi = forms.IntegerField(
    #     label=("Tingkat Depresi"),
    #     # strip=False,
    #     widget=forms.NumberInput(
    #         attrs={
    #             # "placeholder" : "Penanganan",                
    #             "class": "form-control",
    #             "id": "Tingkat Depresi",
    #             "name": "Tingkat Depresi"
    #         }
    #     ),
    # )
    judul = forms.CharField(
        label=("Judul"),
        # strip=False,
        widget=forms.TextInput(
            attrs={
                # "placeholder" : "Penanganan",                
                "class": "form-control",
                "id": "Judul",
                "name": "Judul"
            }
        ),
    )
    image = forms.FileField(
        label=("Cover"),
        # strip=False,
        widget=forms.ClearableFileInput(
            attrs={
                # "placeholder" : "Penanganan",                
                "class": "form-control",
                "id": "Cover",
                "name": "Cover",
            }
        ),
    )
    isi = forms.CharField(
        label=("Isi"),
        # strip=False,
        widget=forms.Textarea(
            attrs={
                # "placeholder" : "Penanganan",                
                "class": "form-control",
                "id": "Isi",
                "name": "Isi"
            }
        ),
    )

    class Meta:
        model = Penanganan
        fields = "__all__"

    # penanganan = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             # "placeholder" : "Penanganan",                
    #             "class": "form-control"
    #         }
    #     ))

    # class Meta:
    #     model = Penanganan
    #     fields = "__all__"

# class ArtikelCreationForm(forms.ModelForm):
#     judul = forms.CharField(
#         label=("Judul"),
#         strip=False,
#         widget=forms.TextInput,
#     )
#     image = forms.FileField(
#         label=("Cover"),
#         strip=False,
#         widget=forms.FileInput,
#     )
#     isi = forms.CharField(
#         label=("Isi"),
#         strip=False,
#         widget=forms.Textarea,
#     )

class ArtikelModelForm(forms.ModelForm):
    judul = forms.CharField(
        label=("Judul"),
        # strip=False,
        widget=forms.TextInput(
            attrs={
                # "placeholder" : "Penanganan",                
                "class": "form-control",
                "id": "Judul",
                "name": "Judul"
            }
        ),
    )
    image = forms.FileField(
        label=("Cover"),
        # strip=False,
        widget=forms.ClearableFileInput(
            attrs={
                # "placeholder" : "Penanganan",                
                "class": "form-control",
                "id": "Cover",
                "name": "Cover",
            }
        ),
    )
    isi = forms.CharField(
        label=("Isi"),
        # strip=False,
        widget=forms.Textarea(
            attrs={
                # "placeholder" : "Penanganan",                
                "class": "form-control",
                "id": "Isi",
                "name": "Isi"
            }
        ),
    )

    class Meta:
        model = Artikel
        fields = "__all__"



class ExportDataForm(forms.ModelForm):
	# export_to_CSV = forms.BooleanField(required=False)
	start_date = forms.DateTimeField(required=False)
	end_date = forms.DateTimeField(required=False)
	class Meta:
		model = HasilDeteksi
		fields = "__all__"