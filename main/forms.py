from django.forms import ModelForm, TextInput, Textarea, DateInput, URLInput
from main.models import Certification

class CertificationForm(ModelForm):
    class Meta:
        model = Certification
        fields = ["title",
                  "issuer",
                  "date_issued",
                  "description",
                  "thumbnail",
        ]

        labels = {
            "title": "Nama Sertifikasi",
            "issuer": "Penerbit Sertifikasi",
            "date_issued": "Tanggal diterbitkan",
            "description": "Deskripsi Sertifikasi",
            "thumbnail": "URL gambar",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Contoh: CS50x", 
                    "maxlength": "255",
                }
            ),
            "issuer": TextInput(
                attrs={
                    "placeholder": "Contoh: Harvard University", 
                    "maxlength": "255",
                }
            ),
            "date_issued": DateInput(
                attrs={
                    "type": "date"
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Deskripsi singkat tentang sertifikasi ini...", 
                    "rows": 3,
                    "maxlength": "500",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://..."
                }
            ),
        }
