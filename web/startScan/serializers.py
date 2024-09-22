from rest_framework import serializers
from .models import ScanHistory


class ScanHistorySerializer(serializers.ModelSerializer):
    """ Serializer for the ScanHistory model """

    class Meta:
        model = ScanHistory
        fields = '__all__'