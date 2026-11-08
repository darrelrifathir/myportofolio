import datetime
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
import datetime

from main.models import Experience, Certification


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        # 1. Periksa halaman HTML menyediakan kerangka grid & pencarian AJAX
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, 'id="grid"')
        self.assertContains(response, 'id="search-input"')

        # 2. Verifikasi data pengalaman dikirim melalui endpoint JSON (kontrak AJAX)
        json_response = self.client.get(reverse("main:get_experiences_json"))
        self.assertEqual(json_response.status_code, 200)
        self.assertContains(json_response, self.experience.title)
        self.assertContains(json_response, self.experience.description)
        self.assertContains(json_response, "part-time")

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))
        self.assertContains(response, "Belum ada pengalaman yang ditambahkan")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        self.assertFalse(self.experience.is_ongoing)

        # Di AJAX, status is_ongoing dievaluasi melalui endpoint JSON
        json_response = self.client.get(reverse("main:get_experiences_json"))
        self.assertEqual(json_response.status_code, 200)
        self.assertContains(json_response, '"is_ongoing": false')

    def test_url_and_template_certification(self):
        response = self.client.get(reverse("main:show_certification"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "certification.html")

    def test_empty_certification_data(self):
        response = self.client.get(reverse("main:show_certification"))
        # Sesuaikan dengan teks persis yang ada di certification.html tanpa tanda titik
        self.assertContains(response, "Belum ada sertifikasi yang ditambahkan")

        # Verifikasi juga endpoint API mengembalikan daftar kosong
        api_response = self.client.get(reverse("api:certification-list"))
        self.assertEqual(api_response.status_code, 200)
        self.assertEqual(api_response.data, [])

    def test_certification_data_displayed(self):
        Certification.objects.create(
            title="Software Engineering Fundamentals",
            issuer="Udemy",
            date_issued=datetime.date(2026, 1, 1),
            description="Pelatihan dasar mengenai pengembangan perangkat lunak",
        )
        # Template HTML menyediakan kerangka grid AJAX
        response = self.client.get(reverse("main:show_certification"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "certification.html")
        self.assertContains(response, 'id="grid"')

        # Verifikasi data sertifikasi berhasil diambil melalui endpoint REST API
        api_response = self.client.get(reverse("api:certification-list"))
        self.assertEqual(api_response.status_code, 200)
        self.assertEqual(len(api_response.data), 1)
        self.assertEqual(
            api_response.data[0]["title"], "Software Engineering Fundamentals"
        )
        self.assertEqual(api_response.data[0]["issuer"], "Udemy")