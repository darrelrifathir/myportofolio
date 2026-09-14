# Create your views here.
from django.shortcuts import render

from main.models import Experience, Certification


def show_main(request):
    context = {
        "name": "Darrel Rifathir Arwa",
        "npm": "2506536420",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Darrel Rifathir Arwa",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_certification(request):
    certifications = Certification.objects.all()
    context = {
        "name": "Darrel Rifathir Arwa",
        "certifications": certifications
    }
    return render(request, "certification.html", context)