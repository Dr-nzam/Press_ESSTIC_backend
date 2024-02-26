from rest_framework import serializers
from informations.models import Information

class InformationSerialiserInput(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ['titre', 'description','image']