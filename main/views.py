# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from main.models import Experience, Certification
from main.forms import CertificationForm
from django.http import HttpResponse
from django.core import serializers


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
    json_response = get_certifications_json(request)
    
    certifications = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    
    certifications = [cert.object for cert in certifications]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Darrel Rifathir Arwa",
        "certifications": certifications,
        "title_query": title_query, 
    }
    return render(request, "certification.html", context)

def create_certification(request):
    form = CertificationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "ertifikasi baru berhasil ditambahkan")
        return redirect("main:show_certification")

    context = {
        "name": "Darrel Rifathir Arwa",
        "form": form,
    }

    return render(request, "certification_form.html", context)

def get_certifications_json(request):
    title_query = request.GET.get("title", "").strip()
    certifications = Certification.objects.all()
    
    if title_query:
        certifications = certifications.filter(title__icontains=title_query)
        
    certifications_json = serializers.serialize("json", certifications)
    
    return HttpResponse(certifications_json, content_type="application/json")

def delete_certification(request, certification_id):
    certification = get_object_or_404(Certification, pk=certification_id)
    
    if request.method == "POST":
        certification.delete()
        messages.success(request, "Sertifikasi berhasil dihapus!")
        
    return redirect("main:show_certification")