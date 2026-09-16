from django.urls import path

from main.views import show_main, show_experience, show_certification, create_certification, get_certifications_json, delete_certification

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("certification/", show_certification, name="show_certification"),
    path("certification/add/", create_certification, name="create_certification"),
    path("api/certifications/", get_certifications_json, name="get_certifications_json"),
    path("certifications/<uuid:certification_id>/delete/", delete_certification, name="delete_certification"),
]