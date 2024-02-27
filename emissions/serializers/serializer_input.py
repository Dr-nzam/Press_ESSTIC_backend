from rest_framework import serializers
from emissions.models import Emissions

class EmissionSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Emissions
        fields = ['nom','image','video','audio']