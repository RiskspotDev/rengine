from rest_framework import serializers
from .models import EngineType


class EngineTypeSerializer(serializers.ModelSerializer):
    """ Serializer for the EngineType model """

    class Meta:
        model = EngineType
        exclude = ['engine_name', 'yaml_configuration']