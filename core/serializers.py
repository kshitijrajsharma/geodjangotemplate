from rest_framework import serializers
from .models import location
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class locationSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = location
        fields = ( 'id',)
        geo_field = "latlng"