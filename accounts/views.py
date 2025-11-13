from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import *
from rest_framework import status

@api_view(["POST"])
@permission_classes([AllowAny])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"User created"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )

        

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    data = request.data
    username = request.data.get("username")
    password = request.data.get("password")
    if not username or not password:
        return Response({"error":"username and password must be set"})
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        serializer = LoginSerializer(user)
        return Response({'message': 'Logged in successfuly'})
    else:
        return Response({'error': 'Invalid credentials'}, status=400)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'message': "User logged out"}, status=status.HTTP_204_NO_CONTENT)
