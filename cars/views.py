from django.shortcuts import render
from rest_framework import viewsets
from .serializer import Car_Serializers
from .models import Cars
# Create your views here.

class Cars_Viewset(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = Car_Serializers

class Mercedes_Viewset(viewsets.ModelViewSet):
    queryset = Cars.objects.filter(car_type='Mercedes')
    serializer_class = Car_Serializers

class BMW_Viewset(viewsets.ModelViewSet):
    queryset = Cars.objects.filter(car_type='BMW')
    serializer_class = Car_Serializers

class  Chevrolet_Viewset(viewsets.ModelViewSet):
    queryset = Cars.objects.filter(car_type='Chevrolet')
    serializer_class = Car_Serializers