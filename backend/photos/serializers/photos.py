from rest_framework import serializers
from backend.photos.models import Photos

class PhotoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    description = serializers.CharField(required=False, allow_blank=True, max_length=100)
    keywords = serializers.CharField(required=False, allow_blank=True, max_length=100)
    url = serializers.CharField(required=False, allow_blank=True, max_length=100)

    def create(self, validated_data):
        """
        Create and return a new `Photos` instance, given the validated data.
        """
        return Photos.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Photos` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.keywords = validated_data.get('keywords', instance.keywords)
        instance.url = validated_data.get('url', instance.url)
        instance.save()
        return instance