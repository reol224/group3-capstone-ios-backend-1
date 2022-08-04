from rest_framework import viewsets, permissions
from backend.photos.serializers.photos import PhotoSerializer
from backend.photos.models import Photos


class PhotosViewSet(viewsets.ModelViewSet):
    queryset = Photos.objects.all().order_by('-ts_created')
    serializer_class = PhotoSerializer
    authentication_classes = ()
    permission_classes = (permissions.AllowAny,)
