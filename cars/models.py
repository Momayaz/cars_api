from django.db import models

# Create your models here.

class Cars(models.Model):

    def __str__(self):
        return self.car_name

    car_name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)
    car_desc = models.CharField(max_length=1000)
    car_price = models.IntegerField()
    car_image = models.ImageField(upload_to='image/', default='image/None/noimg.jpg')