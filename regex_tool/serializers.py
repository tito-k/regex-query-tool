from rest_framework import serializers
from .models import RegexQuery

class RegexQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = RegexQuery
        fields = '__all__'
