from rest_framework import serializers
from tournois.models import Tournois

class TournoisSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Tournois
        fields = ['nom','date','lieu','participant','description']
        