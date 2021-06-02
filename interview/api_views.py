from rest_framework import serializers
from .models import User, Subscribe
from rest_framework.response import Response
from rest_framework import status
from .serializers import PersonSerializer, SubscribeSerializer
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.exceptions import ErrorDetail
from django.core.mail import send_mail
from mock_interview.settings import EMAIL_HOST_USER


class EmailCreate(CreateAPIView, GenericViewSet):

    @api_view(["POST"],)
    def create_person_view(request):
        # user = request.User
        # serializer = PersonSerializer
        try:
            person = User.objects

        except User.DoesNotExist:
            response_message = {"error": "There is no user created for this user."}
            return Response(response_message, status=status.HTTP_400_BAD_REQUEST)

        
        if request.method == "POST":
            serializer = PersonSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data["first_name"] = user.first_name
            data["last_name"] = user.last_name
            data["email"] = user.email
            data["password"] = user.password
            data["phone"] = user.phone
            return Response(data=data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    @api_view(["POST"],)
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
                send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
                return Response(data=data, status=status.HTTP_201_CREATED)
            else:
                data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)