from rest_framework import serializers
from tournois.models import Tournois

class TournoisSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Tournois
        fields = '__all__'