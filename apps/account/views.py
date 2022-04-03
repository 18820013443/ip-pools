from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Account
from .utils.jwt_auth import create_token
from .serializers import CreateAccountSerializer


class LoginView(APIView):

    # @action(methods=['POST'], detail=False, url_path='login')
    # def send_token(self, request, pk=None):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = Account.objects.filter(username=username, password=password).first()
        if not user:
            return Response({"code": 1000, 'error': '用户名或密码错误'})
        payload = {
            'username': username
        }
        serializer = CreateAccountSerializer(instance=user)
        serializer.get_token(user)
        return Response(serializer.data)


class AccountView(APIView):

    def post(self, request):
        data = request.data
        serializer = CreateAccountSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
