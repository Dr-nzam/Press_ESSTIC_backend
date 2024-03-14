from rest_framework import serializers
from account.serializers.serializer import UserSerializerUtilisateurSimpleGet
from informations.models import Information



class InformationSerialiserOut(serializers.ModelSerializer):
    user = UserSerializerUtilisateurSimpleGet()
    class Meta:
        model = Information
        fields = ['titre', 'description','image','user']