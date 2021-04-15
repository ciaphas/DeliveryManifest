from rest_framework import serializers

from .models import warehouse

class WarehouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = warehouse
        fields = ('title', 'forename', 'surname', 'address', 'address2', 'city', 'postcode', 'items', 'con_number', 'deliverycompany')