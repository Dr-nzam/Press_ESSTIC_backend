from rest_framework import serializers
from evenements.models import Evenement

class EvenementSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Evenement
        fields = ['nom', 'date', 'heureDebut', 'heureFin', 'lieu', 'description', 'image']