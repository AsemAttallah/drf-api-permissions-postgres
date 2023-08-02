from django.shortcuts import render
from .models import Car, Post
from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView, RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import CarSerializer, PostSerializer
from rest_framework.permissions import AllowAny
from .permissions import IsOwner
# Create your views here.

class CarListView(ListCreateAPIView) :
    queryset = Car.objects.all()
    serializer_class= CarSerializer

class CarDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class= CarSerializer
    permission_classes=[IsOwner]
# class CarDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Car.objects.all()
#     serializer_class= CarSerializer
# PostListView, PostDetailView
class PostListView(ListCreateAPIView) :
    queryset = Post.objects.all()
    serializer_class= PostSerializer
    permission_classes=[AllowAny]

class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class= PostSerializer
    permission_classes=[AllowAny]