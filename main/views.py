# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from main.models import Experience, Certification
from main.forms import CertificationForm
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
import datetime
from django.contrib.auth.decorators import login_required  # Tambahkan baris ini
from django.core.exceptions import PermissionDenied        # Tambahkan baris ini


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Darrel Rifathir Arwa",
        "npm": "2506536420",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Mahasiswa Ilmu Komputer Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
        "last_login": last_login,
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

@login_required(login_url="/login/")
def create_certification(request):
    # Dua baris berikut yang ditambahkan pada langkah ini.
    # Cek apakah akun yang sedang login adalah superuser (admin/kamu);
    # kalau bukan, hentikan permintaannya dengan 403.
    if not request.user.is_superuser:
        raise PermissionDenied
    
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
    
    certifications_json = serializers.serialize("json", certifications, use_natural_foreign_keys=True)
    return HttpResponse(certifications_json, content_type="application/json")

@login_required(login_url="/login/")
def delete_certification(request, certification_id):
    # Dua baris berikut yang ditambahkan pada langkah ini.
    # Cek apakah akun yang sedang login adalah superuser (admin/kamu);
    # kalau bukan, hentikan permintaannya dengan 403.
    if not request.user.is_superuser:
        raise PermissionDenied
    
    certification = get_object_or_404(Certification, pk=certification_id)
    
    if request.method == "POST":
        certification.delete()
        messages.success(request, "Sertifikasi berhasil dihapus!")
        
    return redirect("main:show_certification")

@login_required(login_url="/login/")
def edit_certification(request, certification_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    certification = get_object_or_404(Certification, pk=certification_id)
    # Isi form dengan instance data lama (jika request GET) atau data baru (jika POST)
    form = CertificationForm(request.POST or None, instance=certification)

    if request.method == "POST":
        form.save()
        messages.success(request, "Sertifikasi Anda berhasil diperbarui")
        return redirect("main:show_certification")

    context = {
        "name": "Darrel Rifathir Arwa",
        "form": form,
        "certification": certification,
    }

    return render(request, "edit_certification.html", context)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Darrel Rifathir Arwa",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Darrel Rifathir Arwa",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

# Tanpa cek is_superuser: semua akun yang sudah login boleh memberi star
@login_required(login_url="/login/")
def toggle_star(request, certification_id):
    certification = get_object_or_404(Certification, pk=certification_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in certification.starred_by.all():
            certification.starred_by.remove(request.user)
        else:
            certification.starred_by.add(request.user)

    return redirect("main:show_certification")