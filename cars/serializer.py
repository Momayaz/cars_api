from rest_framework import serializers
from .models import Cars

class Car_Serializers(serializers.ModelSerializer):
    car_image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Cars
        fields = ['car_name', 'car_type', 'car_desc', 'car_price', 'car_image']