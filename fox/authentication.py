import jwt
from rest_framework.authentication import BaseAuthentication
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed



class CustomJWTAuthentication(BaseAuthentication):
   def authenticate(self, request):
       User = get_user_model()
       authorization_header = request.headers.get('Authorization')
       if not authorization_header:
           return None
       try:
           access_token = authorization_header.split(' ')[1]
           payload = jwt.decode(
               access_token, settings.SECRET_KEY, algorithms=['HS256'])
       except jwt.ExpiredSignatureError:
           raise AuthenticationFailed('Token de acesso expirado')
       except IndexError:
           raise AuthenticationFailed('Token Invalido')
       user = User.objects.filter(id=payload['user_id']).first()
       if user is None:
           raise AuthenticationFailed('Usuário não encontrado')
       if not user.is_active:
           raise AuthenticationFailed('Conta de usuário inativada')
       return (user, None)
