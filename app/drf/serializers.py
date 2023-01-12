from rest_framework import serializers
from .models import WarehouseDRF

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseDRF
        fields = ('id', 'object_name', 'number_of_objects')