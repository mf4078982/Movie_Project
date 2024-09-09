from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MovieModel(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="movies")
    description = models.CharField(max_length=50)  # Updated max_length
    image = models.ImageField(upload_to='images/')



