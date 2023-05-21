from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .serializers import UserSerializers
from rest_framework.response import Response
from .models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from rest_framework.decorators import APIView, api_view, permission_classes
from opera.forms import UserForm
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = UserForm()

    context = {
        'form': form,

    }

    return render(request, 'home.html', context)


def login(request):
    username = request.user
    context = {
        'username': username
    }
    return render(request, 'login.html', context)


def login_user(request):
    form = UserCreationForm()
    return render(request, 'log.html', {'form': form})


#
# class Register(APIView):
#     def post(self, request):
#         serializer = UserSerializers(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#
#
# class LoginView(APIView):
#     def post(self, request):
#         phone_number = request.data['phone_number']
#         password = request.data['password']
#         user = User.objects.filter(phone_number=phone_number)
#         if user is None:
#             raise AuthenticationFailed('user not found')
#         # if not user.check_password(password):
#         #     raise AuthenticationFailed('incorrect password')
#         payload = {
#             'id': user.id,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#             'iat': datetime.datetime.utcnow()
#         }
#         token = jwt.encode(payload, 'secret', algorithm='HS256')
#
#         response = Response()
#         response.set_cookie(key='jwt', value=token, httponly=True)
#
#         response.data = {
#             'jwt': token
#         }
#
#         return response
#
#
# class UserView(APIView):
#     def get(self, request):
#         token = request.COOKIES.get('jwt')
#         if not token:
#             raise AuthenticationFailed('unautheticated')
#         try:
#             payload = jwt.decode(token, 'secret', algorithms=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticate!')
#         user = User.objects.get(id=payload['id']).first()
#         serializer = UserSerializers(user)
#
#         return Response(serializer.data)
@api_view(['POST', ])
def registration_user(request):
    if request.method == 'POST':
        serializer = UserSerializers(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = 'successfully new user created'
            data['phone'] = user.name
            data['phone'] = user.phone_number
        else:
            data = serializer.errors
        return Response(data)
