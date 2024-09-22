from rest_framework import serializers
from .models import Domain


class DomainSerializer(serializers.ModelSerializer):
    """ Serializer for the Domains model """

    class Meta:
        model = Domain
        fields = '__all__'
        # fields = ('id', 'name', 'domain',)