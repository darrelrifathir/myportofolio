from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsPortfolioOwnerOrReadOnly(BasePermission):
    """
    Hanya pemilik portofolio (superuser) yang dapat memodifikasi sertifikasi.
    Pengunjung anonim dan user biasa hanya memiliki hak baca (GET, HEAD, OPTIONS).
    """
    message = "Hanya pemilik portofolio yang dapat memodifikasi sertifikasi."

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS
            or request.user.is_superuser
        )

class IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):
    """
    Hak akses 4 peran:
    - Guest & User biasa : Hanya SAFE_METHODS (GET, HEAD, OPTIONS).
    - Editor             : SAFE_METHODS + PUT/PATCH (tidak bisa POST/DELETE).
    - Superuser          : Akses penuh (GET, POST, PUT, PATCH, DELETE).
    """
    message = "Hanya pemilik portofolio atau Editor yang dapat mengubah sertifikasi."

    def has_permission(self, request, view):
        # 1. Siapa saja (termasuk anonim) boleh membaca data
        if request.method in SAFE_METHODS:
            return True
        
        # 2. Mutasi data wajib sudah terautentikasi (login)
        if not request.user.is_authenticated:
            return False
        
        # 3. Superuser (pemilik portofolio) memiliki akses penuh
        if request.user.is_superuser:
            return True
        # 4. Editor hanya diizinkan mengubah data (PUT / PATCH)
        return (
            request.method in ("PUT", "PATCH")
            and request.user.groups.filter(name="Editor").exists()
        )