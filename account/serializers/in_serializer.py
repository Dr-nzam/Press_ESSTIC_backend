from rest_framework import serializers


class LogoutSerializer(serializers.Serializer):
    token = serializers.CharField(max_length = 128)
        

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)