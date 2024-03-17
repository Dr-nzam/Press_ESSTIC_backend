from rest_framework import serializers
from account.serializers.serializer import UserSerializerUtilisateurSimpleGet
from tournois.models import Tournois

class TournoisSerializerGet(serializers.ModelSerializer):
    user = UserSerializerUtilisateurSimpleGet()
    class Meta:
        model = Tournois
        fields = ['id','nom','date','lieu','image','participant','description', 'user']