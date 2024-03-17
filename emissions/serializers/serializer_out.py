from rest_framework import serializers
from account.serializers.serializer import UserSerializerUtilisateurSimpleGet
from emissions.models import Emissions

class EmissionSerializerGet(serializers.ModelSerializer):
    user = UserSerializerUtilisateurSimpleGet()
    class Meta:
        model = Emissions
        fields = ['id','nom','image','video','audio', 'user']