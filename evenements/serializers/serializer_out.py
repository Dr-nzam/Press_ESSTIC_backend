from rest_framework import serializers
from evenements.models import Evenement


class EvenementSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Evenement
        fields = '__all__'
        
        