from django.db import models

# Create your models here.

class WantModel(models.Model):
    field = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    memo = models.TextField() 

    
    
