from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Certification
from main.permissions import IsPortfolioOwnerOrEditorOrReadOnly
from main.serializers import CertificationSerializer


@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def certification_list(request):
    if request.method in ("GET", "HEAD"):
        certifications = (
            Certification.objects.prefetch_related("starred_by")
            .order_by("title", "id")
        )
        title = request.query_params.get("title", "").strip()
        if title:
            certifications = certifications.filter(title__icontains=title)
        serializer = CertificationSerializer(
            certifications, many=True, context={"request": request}
        )
        return Response(serializer.data)

    serializer = CertificationSerializer(
        data=request.data, context={"request": request}
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def certification_detail(request, certification_id):
    cert = get_object_or_404(
        Certification.objects.prefetch_related("starred_by"), pk=certification_id
    )
    if request.method in ("GET", "HEAD"):
        serializer = CertificationSerializer(cert, context={"request": request})
        return Response(serializer.data)

    if request.method == "DELETE":
        cert.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = CertificationSerializer(
        cert,
        data=request.data,
        partial=(request.method == "PATCH"),
        context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def certification_star(request, certification_id):
    cert = get_object_or_404(Certification, pk=certification_id)
    if cert.starred_by.filter(pk=request.user.pk).exists():
        cert.starred_by.remove(request.user)
    else:
        cert.starred_by.add(request.user)
    serializer = CertificationSerializer(cert, context={"request": request})
    return Response(serializer.data)