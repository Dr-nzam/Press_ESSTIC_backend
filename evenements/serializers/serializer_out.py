from rest_framework import serializers
from account.serializers.serializer import UserSerializerUtilisateurSimpleGet
from evenements.models import Evenement


class EvenementSerializerGet(serializers.ModelSerializer):
    user = UserSerializerUtilisateurSimpleGet()
    class Meta:
        model = Evenement
        fields = ['id','nom', 'date', 'heureDebut', 'heureFin', 'lieu', 'description', 'image', 'user']
        
        