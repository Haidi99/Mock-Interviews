from rest_framework import serializers
from .models import Subscribe
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from .serializers import SubscribeSerializer, RegisterSerializer, UserSerializer, ChangePasswordSerializer, \
    UpdateUserSerializer
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import ErrorDetail
from django.core.mail import send_mail
from mock_interview.settings import EMAIL_HOST_USER
from rest_framework.permissions import IsAuthenticated
from knox.models import AuthToken
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

import schedule 
import time 
import requests


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UpdateProfileView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)  # responsible for login.
        return super(LoginAPI, self).post(request, format=None)


class EmailCreate(CreateAPIView, GenericViewSet):

    # @api_view(["POST"],)
    # def create_person_view(request):
    #     # user = request.User
    #     # serializer = PersonSerializer

    #     try:
    #         person = User.objects

    #     except User.DoesNotExist:
    #         response_message = {"error": "There is no user created for this user."}
    #         return Response(response_message, status=status.HTTP_400_BAD_REQUEST)

    #     if request.method == "POST":
    #         serializer = PersonSerializer(data=request.data)
    #     data = {}
    #     if serializer.is_valid():
    #         user = serializer.save()
    #         data["first_name"] = user.first_name
    #         data["last_name"] = user.last_name
    #         data["email"] = user.email
    #         data["password"] = user.password
    #         data["phone"] = user.phone
    #         return Response(data=data, status=status.HTTP_201_CREATED)
    #     else:
    #         data = serializer.errors
    #     return Response(data, status=status.HTTP_400_BAD_REQUEST) 

    @api_view(["POST"], )
    def create_subscribe_view(request):

        exists = Subscribe.objects
        # if exists:
        #     err = ErrorDetail(string="Email address already used.", code="unique")
        #     response_message = {"email": [err]}
        #     return Response(response_message, status=status.HTTP_400_BAD_REQUEST)

        if request.method == "POST":
            serializer = SubscribeSerializer(data=request.data)
            data = {}
            if serializer.is_valid():
                user = serializer.save()
                data["email"] = user.email
                # send an email
                subject = 'Welcome to Oursite'
                message = 'Hope you are well now, i love you!'
                recepient = str(data['email'])
                send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)

                url = "https://www.careeronestop.org/JobSearch/Interview/interview-tips.aspx"
                # page = requests.get(url)

                def send_tips():
                    subject = 'Mock Interview Tips & trick'
                    message = 'Hello it tips and tricks for this week, please read it and stay tuned for more..'+ url
                    recepient = str(data['email'])
                    return send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
                
                schedule.every(60).seconds.do(send_tips)
                #schedule.every(604800).day().at("06:54").do(send_tips)
                while time:
                    schedule.run_pending()
                    time.sleep(1)


                return Response(data=data, status=status.HTTP_201_CREATED)
            else:
                data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

