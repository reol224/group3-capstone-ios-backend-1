from django.conf.urls import url
from rest_framework import routers
from django.urls import include
from .restful import photos

router = routers.DefaultRouter()

router.register(r'', photos.PhotosViewSet, basename="photos")

urlpatterns = [
    url(r'', include(router.urls)),
]

urlpatterns += router.urls