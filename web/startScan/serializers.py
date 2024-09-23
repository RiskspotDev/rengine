from rest_framework import serializers
from .models import ScanHistory, ScanActivity, CountryISO


class ScanHistorySerializer(serializers.ModelSerializer):
    """ Serializer for the ScanHistory model """

    class Meta:
        model = ScanHistory
        fields = '__all__'


class MostRecentScanSerializer(serializers.ModelSerializer):
    """ Serializer for the MostRecentScan model """

    class Meta:
        model = ScanHistory
        exclude = ['start_scan_date', 'domain', 'scan_type', 'emails', 'employees', 'buckets', 'dorks']


class ScanActivitySerializer(serializers.ModelSerializer):
    """ Serializer for the ScanActivity model """

    class Meta:
        model = ScanActivity
        exclude = ('title', 'name', 'time', 'status')


class CountryISOSerializer(serializers.ModelSerializer):
    """ Serializer for the CountryISO model """

    class Meta:
        model = CountryISO
        fields = '__all__'