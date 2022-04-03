from rest_framework_mongoengine.serializers import DynamicDocumentSerializer
from rest_framework import serializers
from .models import Account
from .utils.jwt_auth import create_token
from rest_framework_mongoengine import fields


class CreateAccountSerializer(DynamicDocumentSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = Account
        fields = ['id', 'username', 'token']
        # extra_kwargs = {'token': {'write_only': True}}

    def get_token(self, userObject):
        payload = {
            'username': userObject.username
        }
        token = create_token(payload)
        return token

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        # user = Account.objects.create(username=username, password=password)
        user = Account(username=username, password=password)
        user.save()
        self.get_token(user)
        return user
