from django.shortcuts import render
from rest_framework import generics
from .models import AppModel
from serializer import AppModelSerializer

# Create your views here.
class List(generics.ListAPIView):
    queryset = AppModel.objects.all()
    serializer_class = AppModelSerializer