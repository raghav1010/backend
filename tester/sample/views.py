from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import mixins,viewsets,status
from rest_framework.generics import GenericAPIView
from .serializers import *
from rest_framework import status
from .models import User
import random
from rest_framework.decorators import action,api_view
from django.shortcuts import get_object_or_404

class LoginAPIView(viewsets.ViewSet):
    # permission_classes = (IsAuthenticated,)  # Must include it to test user is authenticated 
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs): # will get user instance 
        auth_token = self.request.user
        try:
            decoded_token = jwt.decode(auth_token,options={"verify_signature":False})
        except (jwt.DecodeError,jwt.InvalidAlgorithmError):
            raise AuthenticationFailed('Invalid Token')
        
        phone = decoded_token['phone_number']
        
        random_password = str(random.randint(0, 1000))
        name = self.request.data["name"]
        serializer = self.serializer_class(data={'name':name,'password':random_password,'phone':phone})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_created)

        return Response(status=status.HTTP_400_BAD_REQUEST) 
    
    
    def list(self,request):

        auth_token = self.request.user 
        try:
            decoded_token = jwt.decode(auth_token,options={"verify_signature":False})
        except (jwt.DecodeError,jwt.InvalidAlgorithmError):
            raise AuthenticationFailed('Bad Token')
        
        phone = decoded_token['phone_number']
        user = get_object_or_404(self.queryset,phone=phone)
        serializer = self.serializer_class(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def perform_update(self,serializer):
        serializer.save()
    
    def update(self,request):
        partial = True 
        auth_token = self.request.user 
        try:
            decoded_token = jwt.decode(auth_token,options={"verify_signature":False})
        except (jwt.DecodeError,jwt.InvalidAlgorithmError):
            raise AuthenticationFailed('Bad Token')
        name = self.request.data['name']
        phone = decoded_token['phone_number']
        user = get_object_or_404(self.queryset,phone=phone)
        serializer = self.serializer_class(user,data=request.data,partial=partial)
        serializer.is_valid()
        self.perform_update(serializer)

        return Response(serializer.data,status=status.HTTP_200_OK)
    
    





# DRF settings



    