from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField(max_length=4)
    car_img = RichTextField()
    type = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=20)
    engine_size = models.CharField(max_length=10)
    fuel_type = models.CharField(max_length=10)
    features = models.CharField(max_length=255)