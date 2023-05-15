from rest_framework import serializers
from .models import  Url

class UrlSerializer(serializers.Serializer):
    model = Url
    url = serializers.URLField()
    status_code = serializers.IntegerField()