from rest_framework import serializers
from .models import (ScanHistory,
                     ScanActivity,
                     CountryISO,
                     Subdomain,
                     IpAddress,
                     Technology,
                     DirectoryScan,
                     Waf,
                     Port,
                     SubScan,)
from targetApp.models import Domain

from api.serializers import PortSerializer, SubdomainSerializer
from scanEngine.models import EngineType


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
        exclude = ('title', 'name', 'time', 'status',)


class CountryISOSerializer(serializers.ModelSerializer):
    """ Serializer for the CountryISO model """

    class Meta:
        model = CountryISO
        fields = '__all__'

class TechnologySerializer(serializers.ModelSerializer):
    """ Serializer for the Technology model """

    class Meta:
        model = Technology
        fields = '__all__'


class SubScanSerializer(serializers.ModelSerializer):
    """ Serializer for the Subscan model """

    scan_history = ScanHistorySerializer(many=True, read_only=True)
    subdomain = SubdomainSerializer()
    engine = EngineType()
    subdomain_subscan_ids = SubdomainSerializer(many=True, read_only=True)

    class Meta:
        model = SubScan
        fields = '__all__'


class IpAddressSerializer(serializers.ModelSerializer):
    """ Serializer for the IpAddress model """

    ports = PortSerializer(many=True, read_only=True)
    geo_iso = CountryISOSerializer(required=False)
    ip_subscan_ids = SubScanSerializer(many=True, read_only=True)

    class Meta:
        model = IpAddress
        fields = '__all__'


class DirectoryScanSerializer(serializers.ModelSerializer):
    """ Serializer for the DirectoryScan model """

    class Meta:
        model = DirectoryScan
        fields = '__all__'


class WafSerializer(serializers.ModelSerializer):
    """ Serializer for the Waf model """
    class Meta:
        model = Waf
        fields = '__all__'


class DomainSerializer(serializers.ModelSerializer):
    """ Serializer for the DomainModel """
    class Meta:
        model = Domain
        fields = '__all__'
