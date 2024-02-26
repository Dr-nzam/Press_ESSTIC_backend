from rest_framework import serializers
from informations.models import Information

class InformationSerialiserOut(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'