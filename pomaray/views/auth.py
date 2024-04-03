from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from pomaray.serializers.auth import UserSerializer
from pomaray.models.user import User
import jwt, datetime
from django.http import JsonResponse
from django.views import View


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()
        
        response.set_cookie(key='token', value=token, httponly=True)
        response.data = {
            "token": token
        }
        
        return response
    

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)
    
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('token')
        response.data = {
            'message': 'success'
        }
        return response
    

class verifyToken(View):
    def get(self, request):
        token = request.COOKIES.get('token')

        if not token:
            raise PermissionDenied({'message': 'Unauthenticated!'})

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise PermissionDenied({'message': 'Unauthenticated!'})

        try:
            user = User.objects.get(id=payload['id'])
        except User.DoesNotExist:
            raise PermissionDenied({'message': 'Unauthenticated!'})

        return JsonResponse({
            'id': user.id,
            'email': user.email,
            'username': user.username,
        })
