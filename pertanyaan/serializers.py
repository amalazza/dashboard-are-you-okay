from .models import Pertanyaan
from rest_framework import serializers

class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pertanyaan
        fields = ('pertanyaan')