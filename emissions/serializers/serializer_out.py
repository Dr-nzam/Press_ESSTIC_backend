from rest_framework import serializers
from emissions.models import Emissions

class EmissionSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Emissions
        fields = '__all__'