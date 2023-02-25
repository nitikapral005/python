from email.mime import image
from django.db import models

# Create your models here.
class student(models.Model):
    username = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = "images",null=True)
    
    def _str_(self):
        return self.username
        