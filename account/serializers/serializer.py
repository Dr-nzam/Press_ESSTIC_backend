from rest_framework import serializers
from account.models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        user = self.Meta.model.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class UserSerializerGet(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'number_phone', 'token' ]
        


class UserSerializerUtilisateurSimpleGet(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'number_phone', 'is_staff']
        
    