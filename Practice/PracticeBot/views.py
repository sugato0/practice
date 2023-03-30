
from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics
from .models import User,Command
from rest_framework.views import APIView
from rest_framework.response import Response
from .serialisers import UserSerializer
from drf_spectacular.utils import extend_schema
from .untils import encode_password
from random import randrange
import time
# Create your views here.
class Users(APIView):
    @extend_schema(
            request=UserSerializer,
            responses={204: None},
            methods=["POST"]
    )
    @extend_schema(description='Post in User database', methods=["POST"])
    def post(self,request):
    #     id 
    # FIO 
    # emails
    # emails_verified 
    # password 
    # phone_number
    # bithday
    # colledge
    # proffesion
        try:
            out = User.objects.create(
                id = request.data["id"],
                FIO = request.data["FIO"],
                phone_number = request.data["phone_number"],
                bithday = request.data["bithday"],
                colledge = request.data["colledge"],
                proffesion = request.data["proffesion"],
                emails = request.data["email"],
                password = encode_password(str(randrange(100000,1000000))+str(time.time))
            )
            return Response({"post":"success"})
        
        except Exception as e:
            
            return Response({"posts":"некоррекстный формат данных"})

    
    def get(self,request):
        user_model:User.objects.all()
        
        try:
            user_model = User.objects.get(id = request.data["id"])
            
        except:
            return Response("not such id")
        try:
            return Response({"user":UserSerializer(user_model, many=  False).data})
        except Exception as e:
            print(e)
class Commands(APIView):
    
    @extend_schema(
            request=UserSerializer,
            responses={204: None},
            methods=["POST"]
    )
    @extend_schema(description='Post in User database', methods=["POST"])
    def post(self,request):
    # command_name 

    # type_of_game 

    # nick_name 

    # score 

    # steam 

    # discord
        try:
            out = User.objects.create(
                id = request.data["id"],
                FIO = request.data["FIO"],
                phone_number = request.data["phone_number"],
                bithday = request.data["bithday"],
                colledge = request.data["colledge"],
                proffesion = request.data["proffesion"],
                emails = request.data["emails"],
                password = encode_password(str(randrange(100000,1000000))+str(time.time))
            )
            out = Command.objects.create(
                command_name = request.data["command_name"],
                type_of_game = request.data["type_of_game"],
                nick_name = request.data["nick_name"],
                score = request.data["score"],
                steam = request.data["steam"],
                discord = request.data["discord"],
                emails = request.data["emails"],
                password = encode_password(str(randrange(100000,1000000))+str(time.time))
            )
            return Response({"post":"success"})
        
        except Exception as e:
            
            return Response({"posts":"некоррекстный формат данных"})

    
    # def get(self,request):
    #     users = User.objects.all()
    #     return Response({"users":UserSerializer(users, many= True).data})
    
# class UserProfileAPIView(APIView):
#     @extend_schema(
#             request=UserProfileSerializer,
#             responses={204: None},
#             methods=["POST"]
#     )
#     @extend_schema(description='Post in User_profile database', methods=["POST"])
    
#     def post(self,request):
#         queryset:User.objects.get()
#         try:
#             queryset = User.objects.get(id = request.data["id"])
#         except Exception as e:
#             print(e)
#             return Response("not such id")
        
#         try:
            
#             # out = User_profile.objects.create(
#             #     user = queryset,
#             #     user_name = request.data["name"],
#             #     user_surname = request.data["surname"],
#             #     phone_number = request.data["phone_number"],
#             #     phone_number_verified  = request.data["phone_number_verified"]
#             # )
            
#             return Response("success")
#         except Exception as e:
#             print(e)
#             return Response({"posts":"Not valid Data"})

    
#     def get(self,request):
#         # userProfile_model:User_profile.objects.all()
        
#         try:
#             #userProfile_model = User_profile.objects.get(user = request.data["id"])
#             pass
#         except Exception as e:
#             return Response({"Error":str(e)})
    
#         #return Response({"user_profile":UserProfileSerializer(userProfile_model, many= False).data})


